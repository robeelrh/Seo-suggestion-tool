<?php

namespace App\Services;

use Symfony\Component\Process\Process;

class Envoy
{    
    public $workingDirectory;

    /**
     * @param string $clientId
     */
    public function __construct(string $workingDirectory)
    {
        $this->workingDirectory = $workingDirectory;
    }

    public function run($task, $event = null, $args = [])
    {
        $result = [];
                        
        $process = Process::fromShellCommandline('php ' . config('app.envoy_composer_bin_path') . ' run '. $task);        
        $process->setTimeout(360000000);
        $process->setIdleTimeout(360000000);        
        $process->setWorkingDirectory($this->workingDirectory);                                                            
        $process->run(
            function ($type, $buffer) use ($event, $args, &$result) {
                $buffer = str_replace('[127.0.0.1]: ', '', $buffer);
                $buffer = str_replace('[forge@82.196.11.126]: ', '', $buffer);
                $buffer = str_replace('[ausus]: ', '', $buffer);                
                
                if (!empty($event)) {                          
                    $buffer = explode(PHP_EOL, $buffer);                                        
                    foreach($buffer as $item){
                        if(!empty($item)){
                            $eventArgs = $args;
                            $eventArgs["message"] = $item;                            
                            event(new $event($eventArgs));                    
                        }
                    }                    
                }

                $result[] = $buffer;
            }
        );
                
        return $result;
    }
}