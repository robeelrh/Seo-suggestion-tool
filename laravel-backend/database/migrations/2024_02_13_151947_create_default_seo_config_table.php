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
        Schema::create('default_seo_config', function (Blueprint $table) {
            $table->id();
            $table->unsignedInteger('meta_tag_title_min_length');
            $table->unsignedInteger('meta_tag_title_max_length');
            $table->unsignedInteger('meta_tag_description_min_length');
            $table->unsignedInteger('meta_tag_description_max_length');
            $table->unsignedInteger('max_page_size');
            $table->unsignedInteger('min_page_word_count');
            $table->unsignedInteger('max_h1_header_length');
            $table->unsignedInteger('max_h2_header_length');
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('default_seo_config');
    }
};
