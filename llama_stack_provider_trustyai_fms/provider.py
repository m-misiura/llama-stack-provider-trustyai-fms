import logging

logger = logging.getLogger(__name__)

from llama_stack.providers.datatypes import ProviderSpec, Api

try:
    from llama_stack.providers.datatypes import RemoteProviderSpec
    USE_NEW_API = True
    logger.debug("Using RemoteProviderSpec (llama-stack > 0.22)")
except ImportError:
    from llama_stack.providers.datatypes import AdapterSpec, remote_provider_spec
    USE_NEW_API = False
    logger.debug("Using remote_provider_spec (llama-stack <= 0.22)")

def get_provider_spec() -> ProviderSpec:
    if USE_NEW_API:
        return RemoteProviderSpec(
            api=Api.safety,
            provider_type="remote::trustyai_fms",
            config_class="llama_stack_provider_trustyai_fms.config.FMSSafetyProviderConfig",
            module="llama_stack_provider_trustyai_fms",
            adapter_type="trustyai_fms",
        )
    else:
        return remote_provider_spec(
            api=Api.safety,
            adapter=AdapterSpec(
                adapter_type="trustyai_fms",
                config_class="llama_stack_provider_trustyai_fms.config.FMSSafetyProviderConfig",
                module="llama_stack_provider_trustyai_fms",
            ),
        )


def get_shields_provider_spec() -> ProviderSpec:
    if USE_NEW_API:
        spec = RemoteProviderSpec(
            api=Api.shields,
            provider_type="remote::trustyai_fms",
            config_class="llama_stack_provider_trustyai_fms.config.FMSSafetyProviderConfig",
            module="llama_stack_provider_trustyai_fms",
            adapter_type="trustyai_fms",
        )
    else:
        spec = remote_provider_spec(
            api=Api.shields,
            adapter=AdapterSpec(
                adapter_type="trustyai_fms",
                config_class="llama_stack_provider_trustyai_fms.config.FMSSafetyProviderConfig",
                module="llama_stack_provider_trustyai_fms",
            ),
        )
    
    logger.debug(f"Returning shields provider spec: {spec}")
    return spec