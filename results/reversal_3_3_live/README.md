# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-05-05 01:30:06 EDT`
Last processed slot: `share_ext_0130`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`; off-hours `5-minute` checkpoints continue mark-to-market updates for open positions, while any legacy share positions still held from older versions continue extended-hours take-profit and stop loss scans until flat
- Live exit ladder: `+15% / +15% / -12%`
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries and exits use the current option mark price; no intraday future path is assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$9,107.50`
- Equity: `$17,459.50`
- Realized PnL: `$7,667.50`
- Unrealized PnL: `$-208.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  INTC     option         option INTC260618C00095000       2026-05-04                   1      8      8560.0                  8352.0         10.7          10.44       96.63          95.8          -208.0                  -2.43         100.0               20               3.0         78.24             0.0                  98.58                   NaN          921.0                0.0         manual_override
```

## Today's Closed Trades (2026-05-05)

_None_

## Current Screener Snapshot

_None_

## Recent Events

```text
                    timestamp_et         slot      event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       detail
2026-05-05T01:30:06.241617-04:00       manual manual_override {"entry_option_price": 10.7, "entry_timestamp_et": "2026-05-04T15:31:00-04:00", "fill_source": "manual 10.70 fill within the observed 15:00-16:00 ET INTC option tape range", "new_contract_symbol": "INTC260618C00095000", "new_position_id": "INTC_20260504T153100", "new_ticker": "INTC", "old_contract_symbol": "CHTR260618C00175000", "old_position_id": "CHTR_20260504T145009", "old_ticker": "CHTR", "reason": "user_observed_intc_signal_on_2026_05_04; manual_midpoint_fill_10_70"}
2026-05-05T00:00:06.231478-04:00 data_refresh    data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {'saved': 99}
2026-05-04T16:10:09.757546-04:00  manage_1600    slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "already_processed"}
2026-05-04T16:05:09.908041-04:00  manage_1600    slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "already_processed"}
2026-05-04T16:00:09.839612-04:00  manage_1600    slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "already_processed"}
2026-05-04T15:55:09.975943-04:00  manage_1600    slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "already_processed"}
2026-05-04T15:40:09.372943-04:00  manage_1530    slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "already_processed"}
2026-05-04T15:35:09.467002-04:00  manage_1530    slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "already_processed"}
       2026-05-04T15:31:00-04:00   entry_1500           entry                {"allocated_cash": 8560.0, "asset_type": "option", "contract_symbol": "INTC260618C00095000", "contracts": 8, "entry_option_price": 10.7, "execution_mode": "option", "fill_source": "manual midpoint adjustment within 15:00-16:00 ET option tape range", "matched_signals": 20, "option_liquidity_status": "manual_override", "option_open_interest": null, "option_spread_pct": 0.0, "option_volume": 921.0, "success_rate": 100.0, "ticker": "INTC", "timing_score": null}
2026-05-04T15:30:09.346876-04:00  manage_1530    slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260505013006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260505013006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260505013006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260505013006)

</details>
