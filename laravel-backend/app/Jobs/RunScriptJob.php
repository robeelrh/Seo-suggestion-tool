<?php

namespace App\Jobs;

use Illuminate\Bus\Queueable;
use Illuminate\Contracts\Queue\ShouldQueue;
use Illuminate\Foundation\Bus\Dispatchable;
use Illuminate\Queue\InteractsWithQueue;
use Illuminate\Queue\SerializesModels;
use Symfony\Component\Process\Process;

class RunScriptJob implements ShouldQueue
{
    use Dispatchable, InteractsWithQueue, Queueable, SerializesModels;

    protected $scriptPath;
    protected $arguments;

    public $timeout = null;

    public function __construct($scriptPath, $arguments)
    {
        $this->scriptPath = $scriptPath;
        $this->arguments = $arguments;
    }

    public function handle()
    {
        $args = [];
        foreach ($this->arguments as $key => $value) {
            $args[] = "--{$key}";
            $args[] = "{$value}";
        }

        $process = new Process(
            array_merge(["python3", $this->scriptPath], $args)
        );
        $process->setTimeout(null);
        $process->run();

        if (!$process->isSuccessful()) {
            \Log::error(
                "Script execution failed: " . $process->getErrorOutput()
            );
        } else {
            \Log::info(
                "Script executed successfully: " . $process->getOutput()
            );
        }
    }
}
