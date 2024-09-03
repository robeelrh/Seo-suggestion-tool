<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class ScrapedUrlsData extends Model
{
    use HasFactory;
    protected $table = 'scraped_urls_data';
    protected $fillable = ['key', 'value','page_id' ];
}
