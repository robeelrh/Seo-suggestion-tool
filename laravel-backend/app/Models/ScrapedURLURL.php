<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class ScrapedURLURL extends Model
{
    use HasFactory;
    protected $table = 'scraped_urls_urls';
    protected $fillable = ['scraped_url_id', 'url'];
   
}