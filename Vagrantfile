VAGRANTFILE_API_VERSION = "2"
Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.define "ubuntu-base" do |u|
    u.vm.box = "ubuntu/xenial64"
    u.vm.hostname = "ubuntu-base"
    u.vm.network "public_network"
  end
end