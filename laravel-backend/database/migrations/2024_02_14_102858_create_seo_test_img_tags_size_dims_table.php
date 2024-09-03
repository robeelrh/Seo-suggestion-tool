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
        Schema::create('seo_test_img_tags_size_dims', function (Blueprint $table) {
            $table->id();

            $table->string('url')->nullable();
            $table->integer('scraper_id')->default(0);
            $table->integer('scraped_url_id')->default(0);

            $table->boolean('is_alt_satisfied')->default(true);
            $table->boolean('is_size_satisfied')->default(true);
            $table->boolean('is_dimension_satisfied')->default(true);

            $table->integer('weight')->default(0);

            $table->json('missing_alt_tags')->nullable();
            $table->json('with_alt_tags')->nullable();

            $table->json('correct_size')->nullable();
            $table->json('large_size')->nullable();

            $table->json('correct_dimensions')->nullable();
            $table->json('incorrect_dimensions')->nullable();
            $table->string('suggestion')->nullable();
            
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('seo_test_img_tags_size_dims');
    }
};
