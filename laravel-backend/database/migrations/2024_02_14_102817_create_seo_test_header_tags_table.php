<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        Schema::create('seo_test_header_tags', function (Blueprint $table) {
            $table->id();
            
            $table->string('url')->nullable();
            $table->integer('scraper_id')->default(0);
            $table->integer('scraped_url_id')->default(0);

            $table->boolean('is_satisfied');
            $table->boolean('is_h2_satisfied');
            $table->integer('weight');
            $table->json('headers');
            $table->integer('keyword_count_outside_h1');
            $table->string('suggestion')->nullable();
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('seo_test_header_tags');
    }
};
