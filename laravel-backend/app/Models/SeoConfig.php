<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class SeoConfig extends Model
{
    use HasFactory;
    protected $table = 'default_seo_config';
    protected $fillable = [
        'meta_tag_title_min_length',
        'meta_tag_title_max_length',
        'meta_tag_description_min_length',
        'meta_tag_description_max_length',
        'max_page_size',
        'min_page_word_count',
        'max_h1_header_length',
        'max_h2_header_length',
    ];
}