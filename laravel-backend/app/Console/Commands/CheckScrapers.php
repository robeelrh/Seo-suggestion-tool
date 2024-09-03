<?php

namespace App\Console\Commands;

use Illuminate\Console\Command;
use Illuminate\Support\Facades\DB;
use App\Jobs\RunScriptJob;
use App\Services\ScriptRunner;

class CheckScrapers extends Command
{
    protected $signature = 'check:scrapers';
    protected $description = 'Check for pending scrapers and add them to the queue';

    public function __construct()
    {
        parent::__construct();
    }

    // * * * * * cd /Users/dev/Desktop/extern_component_editor/laravel-backend && php artisan schedule:run >> /dev/null 2>&1

    public function handle(ScriptRunner $scriptRunner)
    {
        $pendingScrapers = DB::table('scrapers')->where('status', 'pending')->where('queued', false)->get();
    
        foreach ($pendingScrapers as $scraper) {
            // Add the job to the queue
            // $args=[];
            $scriptPath = "/Users/dev/Desktop/extern_component_editor/playwright/main.py";
            $arguments = ["scraper_id" => $scraper->id];
            // $args['scriptPath'] = "/Users/dev/Desktop/extern_component_editor/playwright/main.py";
            // $args['arguments'] = ["scraper_id" => $scraper->id];
            RunScriptJob::dispatch($scriptPath, $arguments)
                ->delay(now()->addMinutes(1));

                \Log::info('Dispatching scraper ' . $scraper->id);
    
            // Mark the scraper as queued
            DB::table('scrapers')
                ->where('id', $scraper->id)
                ->update(['queued' => true]);
        }
    }
}