<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class SeoTestImgTagsSizeDim extends Model
{
    protected $table = 'seo_test_img_tags_size_dims';

    protected $fillable = [
        'url', 'scraper_id', 'scraped_url_id',
        'is_alt_satisfied',
        'is_size_satisfied',
        'is_dimension_satisfied',
        'weight',
        'missing_alt_tags',
        'with_alt_tags',
        'correct_size',
        'large_size',
        'suggestion',
        'correct_dimensions',
        'incorrect_dimensions',
    ];
}