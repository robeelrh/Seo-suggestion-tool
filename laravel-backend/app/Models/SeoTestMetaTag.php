<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class SeoTestMetaTag extends Model
{
    protected $table = 'seo_test_meta_tags';

    protected $fillable = [
        'url', 'scraper_id', 'scraped_url_id',
        'is_satisfied',
        'is_description_length_satisfied',
        'is_title_length_satisfied',
        'weight',
        'suggestion',
    ];
}