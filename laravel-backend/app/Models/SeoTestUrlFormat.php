<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class SeoTestUrlFormat extends Model
{
    protected $fillable = [
        'url', 'scraper_id', 'scraped_url_id',
        'is_satisfied',
        'url_length',
        'weight',
        'url_string',
        'suggestion',
    ];
}