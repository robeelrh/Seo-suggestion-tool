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

        Schema::table('scrapers', function (Blueprint $table) {
            $table->boolean('queued')->nullable()->default(false);
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        if (Schema::hasColumn('scrapers', 'queued')) {
            Schema::table('scrapers', function (Blueprint $table) {
                $table->dropColumn('queued');
            });
        }
    }
};
