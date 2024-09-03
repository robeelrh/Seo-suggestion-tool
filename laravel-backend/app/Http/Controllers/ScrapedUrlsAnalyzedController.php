<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\ScrapedUrlsZipFile;

class ScrapedUrlsAnalyzedController extends Controller
{
    public function handle(Request $request)
    {
        $this->validate($request, [
            'scraped_url_id'=>'required',
            'breadcrumb' => 'required',
            'file_size'=> 'required',
            'page_speed'=> 'required',
            'content_percentage'=> 'required',
            'primary_key_percentage'=> 'required',
            'ssl_protocol'=> 'required',
            'valid_till'=> 'required',
            'new_protocol_version' => 'required'
        ]);    
        
        $scrapedUrlsZipFile = new ScrapedUrlsZipFile();

        $scrapedUrlsZipFile->scraped_url_id = $request->get('scraped_url_id');
        $scrapedUrlsZipFile->breadcrumb = $request->get('breadcrumb');
        $scrapedUrlsZipFile->file_size = $request->get('file_size');
        $scrapedUrlsZipFile->page_speed = $request->get('page_speed');
        $scrapedUrlsZipFile->content_percentage = $request->get('content_percentage');
        $scrapedUrlsZipFile->primary_key_percentage = $request->get('primary_key_percentage');
        $scrapedUrlsZipFile->ssl_protocol = $request->get('ssl_protocol');
        $scrapedUrlsZipFile->valid_till = $request->get('valid_till');
        $scrapedUrlsZipFile->new_protocol_version = $request->get('new_protocol_version');

        $scrapedUrlsZipFile->save();

        return response()->json(['message' => 'Data saved'], 200);
    }
}
