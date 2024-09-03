<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class ScrapedNetworkContent extends Model
{
    use HasFactory;
    protected $table = 'scraped_network_content';
    protected $fillable = ['scraped_url_id', 'url', 'status_code', 'time'];
}
