@php
$deploy_servers = ['local' => 'localhost'];
@endphp

@servers($deploy_servers)

@task('command', ['on' => $server])
    {{ $command }}
@endtask