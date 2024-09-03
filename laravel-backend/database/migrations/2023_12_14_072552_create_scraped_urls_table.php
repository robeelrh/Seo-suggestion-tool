<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::create('scraped_urls', function (Blueprint $table) {
            $table->id();
            $table->string('scraped_url');
            $table->unsignedBigInteger('scraper_id')->nullable();
            $table->string('status_code')->nullable();
            $table->string('out_going')->nullable();
            $table->string('redirected_URL')->nullable();
            $table->string('scraper_timestamp')->nullable();
            $table->boolean('indexed')->default(false)->index();

            // Foreign key relationship
            $table->foreign('scraper_id')->references('id')->on('scrapers');
            
            $table->timestamps();
        });
    }

    public function down(): void
    {
        Schema::dropIfExists('scraped_urls');
    }
};