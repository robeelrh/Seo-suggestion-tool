<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class ScrapedUrlsZipFile extends Model
{
    use HasFactory;
    protected $table = 'scraped_urls_analyzed';
    protected $fillable = ['file_size', 'scraped_url_id', 'breadcrumb', 'page_speed', 'content_percentage' ,'primary_key_percentage', 'ssl_protocol', 'valid_till', 'new_protocol_version'];
}