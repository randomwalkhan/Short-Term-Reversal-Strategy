# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-05-06 13:04:07 EDT`
Last processed slot: `manage_1300`

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

- Cash: `$19,842.50`
- Equity: `$19,842.50`
- Realized PnL: `$9,842.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-05-06)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price         pnl  return_pct           exit_reason
  TEAM     option         option TEAM260618C00090000     11          2026-05-05         2026-05-06         9.65         6.7 -3244.99958  -30.569945 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  CHTR           90.24               41            0.55              0.61        157.97               118.74            True
  CDNS           97.30               37            0.70              1.74        352.88                54.11            True
   XEL           90.00               10            1.52              0.87         81.08                28.13            True
  CRWD           81.82               22            1.69              5.64        474.11                50.97            True
    ZS           80.00               25            2.04              2.02        140.49                69.30            True
  MSTR           87.80               41            0.71              0.92        186.50                66.92            True
  ADSK           83.33               12            2.82              4.93        247.32                46.09            True
  TMUS           84.38               32            0.71              0.96        193.94                36.92            True
  FTNT           94.12               34            0.98              0.62         89.66                40.66            True
  PLTR           84.00               25            2.01              1.91        135.09                62.37            True
  PYPL           94.12               34            0.62              0.20         46.39                42.64            True
  PANW           86.11               36            0.75              0.97        183.56                45.58            True
```

## Recent Events

```text
                    timestamp_et           slot     event_type                                                                                                                                                                                                                                                                                                                                                                            detail
2026-05-06T11:37:18.444380-04:00    manage_1130   slot_skipped                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-05-06T10:28:45.392607-04:00    manage_1030           exit                                                                                                                                                                                                  {"asset_type": "option", "contract_symbol": "TEAM260618C00090000", "fill_price": 6.7, "pnl": -3245.0, "reason": "stop_loss_hit_at_scan", "return_pct": -30.57, "ticker": "TEAM"}
2026-05-06T09:35:01.127893-04:00    manage_0930   slot_skipped                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-05-06T00:00:03.652066-04:00   data_refresh   data_refresh                                                                                                                                                                                                                                                                                                                                                                     {'saved': 99}
       2026-05-05T16:01:00-04:00 backfill_audit backfill_audit                                                                                                               {"open_positions_after_backfill": 1, "reason": "Mac was offline; reconstructed missed 2026-05-05 ET afternoon slots using stock and option 1m bars clipped at each slot time", "slots": ["manage_1400", "manage_1430", "entry_1500", "manage_1530", "manage_1600"]}
       2026-05-05T15:00:00-04:00     entry_1500          entry {"allocated_cash": 10615.0, "asset_type": "option", "contract_symbol": "TEAM260618C00090000", "contracts": 11, "entry_option_price": 9.65, "execution_mode": "option", "matched_signals": 38, "option_liquidity_status": "ok", "option_open_interest": 2308.0, "option_spread_pct": 3.81, "option_volume": 583.0, "success_rate": 84.21, "ticker": "TEAM", "timing_score": 0.669}
       2026-05-05T15:00:00-04:00     entry_1500 timing_overlay                                                                                                                                                                                                                                                                      {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-05", "training_samples": 5543, "window": 5}
2026-05-05T13:30:09.549744-04:00    manage_1330   slot_skipped                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-05-05T13:25:09.992302-04:00    manage_1330   slot_skipped                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-05-05T13:10:09.568185-04:00    manage_1300   slot_skipped                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260506130407)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260506130407)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260506130407)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260506130407)

</details>
