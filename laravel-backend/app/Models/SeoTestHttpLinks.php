<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class SeoTestHttpLinks extends Model
{
    protected $fillable = [
        'url', 'scraper_id', 'scraped_url_id',
        'is_satisfied',
        'http_links',
        'weight',
        'suggestion',
    ];
}