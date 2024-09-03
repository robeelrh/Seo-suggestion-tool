<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class ScrapedUrlSiteMapData extends Model
{
    use HasFactory;
    protected $table = 'scraped_urls_site_map_data';
    protected $fillable = ['scraped_url_id', 'scraped_url','site_map_content'];
}
