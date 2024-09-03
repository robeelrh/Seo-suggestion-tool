<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;

Route::middleware('auth:sanctum')->get('/user', function (Request $request) {
    return $request->user();
});

Route::get('/', function () {
    return view('welcome');
});

Route::get('/home', function () {
    return 'Hello World';
});



Route::post('/scrapers/get_all', 'App\Http\Controllers\ScraperGetAllController@handle')->name('get-all-scrapers');
Route::post('/scrapers/get_all_by_project', 'App\Http\Controllers\ScraperGetAllByProjectController@handle')->name('get-all-scrapers-by-project');

Route::post('/scrapers/get_by_id', 'App\Http\Controllers\ScraperGetOneController@handle')->name('get-one-scrapers');
Route::post('/scrapers/update_scraper', 'App\Http\Controllers\ScraperUpdateOneController@handle')->name('update-one-scrapers');

Route::post('/scrapers/create', 'App\Http\Controllers\ScraperCreateController@handle')->name('create-scraper');
Route::post('/scrapers/update_by_id', 'App\Http\Controllers\ScraperUpdateController@handle')->name('update-scraper');
Route::post('/scrapers/delete_by_id', 'App\Http\Controllers\ScraperDeleteController@handle')->name('delete-scraper');

//scraped urls controllers 

Route::post('/scrapers/urls/create', 'App\Http\Controllers\ScrapedURLCreateController@handle')->name('create-scrapedURL');
Route::post('/scrapers/urls_urls/create', 'App\Http\Controllers\ScrapedURLURLCreateController@handle')->name('create-urls-of-scraped-urls');
Route::post('/scraped_url/create_sitemap_data', 'App\Http\Controllers\ScrapedURLSaveSiteMap@handle')->name('save-sitemap-data-scrapedURL');
Route::post('/scrapers/get_famous_links', 'App\Http\Controllers\ScrapedURLGetDepthController@handle')->name('get-most-repeated-link-of-website');

Route::post('/scraped_url/get_by_id', 'App\Http\Controllers\ScrapedURLGetOneController@handle')->name('get-one-scraperd-url');

Route::post('/scrapers/urls/data/create', 'App\Http\Controllers\ScrapedUrlsDataCreateController@handle')->name('create-scrapedURLData');
Route::post('/scrapers/urls/get_scraped_url','App\Http\Controllers\ScrapedURLGetURLsByScrapedURLIDController@handle')->name('get-scrapedURLs-byScrapedURLsId');

Route::post('/scrapers/urls/get_by_session','App\Http\Controllers\ScrapedURLGetBySessionController@handle')->name('get-scrapedURLs-bySessions');
Route::post('/scrapers/urls/store_page_content', 'App\Http\Controllers\ScrapedUrlsAnalyzedController@handle')->name('create-scrapedURLZip');
Route::post('/scrapers/urls/data/get', 'App\Http\Controllers\ScrapedURLDataGetController@handle')->name('get-scrapedURLData');

Route::post('/scrapers/upload/image', 'App\Http\Controllers\ImageUploadController@handle')->name('upload-image');

Route::post('/scrapers/network/create', 'App\Http\Controllers\ScrapedURLNetworkController@handle')->name('save-network-content');

// Dashboard EndPoints

Route::post('/dashboard/get_crawler_speed', 'App\Http\Controllers\DashboardGetCrawlingSpeed@handle')->name('dashboard-get-crawler-speed');
Route::post('/dashboard/get_crawled_urls_count', 'App\Http\Controllers\DashboardCrawledUrlsInfoController@handle')->name('dashboard-get-crawled-urls-count');
Route::post('/dashboard/get_crawling_frequency', 'App\Http\Controllers\DashboardCrawlerFrequencyInfoController@handle')->name('dashboard-get-crawling-frequency');
Route::post('/dashboard/get_scraper_performance', 'App\Http\Controllers\DashboardScraperPerformanceController@handle')->name('dashboard-get-scraper-performance');
Route::post('/dashboard/get_scraper_by_time', 'App\Http\Controllers\DashboardScraperGetByTimeController@handle')->name('get-scraper-by-time');


// Scraper View endpoints
Route::post('/scraper/get_issue_info', 'App\Http\Controllers\ScraperIssueInfoController@handle')->name('scraper-get-issue-info');
Route::post('/scraper/get_page_status_code_status', 'App\Http\Controllers\ScraperPageStatusCodeStatusController@handle')->name('scraper-get-page-status-code-status');
Route::post('/scraper/get_health_info', 'App\Http\Controllers\ScraperHealthInfoController@handle')->name('scraper-get-health-info');





// Projects
Route::post('/project/get_all', 'App\Http\Controllers\ProjectGetAllController@handle')->name('get-all-project');
Route::post('/project/create', 'App\Http\Controllers\ProjectCreateController@handle')->name('create-project');
Route::post('/project/get', 'App\Http\Controllers\ProjectGetController@handle')->name('get-project-details');
Route::post('/project/get_project_scrapers', 'App\Http\Controllers\ProjectGetScrapersController@handle')->name('get-scrapers-of-one-project');
// Route::post('/project/update', 'App\Http\Controllers\ProjectGetController@handle')->name('update-project-details');
// Route::post('/project/delete', 'App\Http\Controllers\ProjectGetController@handle')->name('delete-project-details');

// Seo Config
Route::post('/seo_configuration/create', 'App\Http\Controllers\ConfigCreateController@handle')->name('saving-seo-configurations');
Route::post('/seo_configuration/get', 'App\Http\Controllers\ConfigGetController@handle')->name('get-seo-configurations');

// SEO test
Route::post('/seo/get_images_data', 'App\Http\Controllers\SeoGetImagesTestData@handle')->name('get-data-from-seo-images-table');


//search Index
Route::post('/search_index/get', 'App\Http\Controllers\SearchIndexController@handle')->name('get-search_index');

//Script runner
Route::post('/script_runner/run', 'App\Http\Controllers\ScriptRunnerController@handle')->name('run-script');


// suggestions CRUD
Route::post('/suggestions/create', 'App\Http\Controllers\SuggestionCreateController@handle')->name('suggestion-create');
Route::post('/suggestions/get_all', 'App\Http\Controllers\SuggestionGetAllController@handle')->name('suggestion-get-all');
Route::post('/suggestions/get_one', 'App\Http\Controllers\SuggestionGetOneController@handle')->name('suggestion-get-one');
Route::post('/suggestions/update', 'App\Http\Controllers\SuggestionUpdateController@handle')->name('suggestion-update');
Route::post('/suggestions/delete', 'App\Http\Controllers\SuggestionDeleteController@handle')->name('suggestion-delete');
