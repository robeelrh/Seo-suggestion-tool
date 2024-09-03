<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use App\Models\ScrapedUrlsData;
use App\Models\ScrapedUrlSiteMapData; 

class ScrapedUrls extends Model
{
    use HasFactory;
    protected $table = 'scraped_urls';
    protected $fillable = ['scraper_id', 'scraped_url', 'status_code', 'out_going', 'redirected_URL', 'scraper_timestamp', 'indexed'];
    // Define the 'data' relationship
    public function data()
    {
        return $this->hasMany(ScrapedUrlsData::class,'page_id', 'id');
    }

    public function ScrapedUrlSiteMapData()
    {
        return $this->hasMany(ScrapedUrlSiteMapData::class, 'scraped_url_id', 'id');
    }
}