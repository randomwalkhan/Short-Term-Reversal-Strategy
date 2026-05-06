# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-05-06 11:02:19 EDT`
Last processed slot: `manage_1100`

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
   XEL           94.44               18            0.86              0.49         81.24                28.13            True
    ZS           80.00               20            2.39              2.37        140.35                69.30            True
  CRWD           84.00               25            1.59              5.32        474.25                50.97            True
   KDP           86.36               22            0.93              0.19         28.84                34.27            True
  TMUS           86.21               29            0.85              1.16        193.85                36.92            True
  MSTR           87.18               39            1.32              1.72        186.16                66.92            True
  ADSK           81.82               11            3.00              5.24        247.18                46.09            True
  PYPL           93.33               30            0.74              0.24         46.38                42.64            True
  DDOG           89.29               28            1.77              1.80        144.96                55.69            True
  CHTR           89.58               48            0.11              0.12        158.18               118.74           False
  CDNS           97.62               42            0.05              0.13        353.58                54.11           False
  TEAM           75.00               12            5.24              3.38         90.90               119.37           False
```

## Recent Events

```text
                    timestamp_et           slot     event_type                                                                                                                                                                                                                                                                                                                                                                            detail
2026-05-06T10:28:45.392607-04:00    manage_1030           exit                                                                                                                                                                                                  {"asset_type": "option", "contract_symbol": "TEAM260618C00090000", "fill_price": 6.7, "pnl": -3245.0, "reason": "stop_loss_hit_at_scan", "return_pct": -30.57, "ticker": "TEAM"}
2026-05-06T09:35:01.127893-04:00    manage_0930   slot_skipped                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-05-06T00:00:03.652066-04:00   data_refresh   data_refresh                                                                                                                                                                                                                                                                                                                                                                     {'saved': 99}
       2026-05-05T16:01:00-04:00 backfill_audit backfill_audit                                                                                                               {"open_positions_after_backfill": 1, "reason": "Mac was offline; reconstructed missed 2026-05-05 ET afternoon slots using stock and option 1m bars clipped at each slot time", "slots": ["manage_1400", "manage_1430", "entry_1500", "manage_1530", "manage_1600"]}
       2026-05-05T15:00:00-04:00     entry_1500          entry {"allocated_cash": 10615.0, "asset_type": "option", "contract_symbol": "TEAM260618C00090000", "contracts": 11, "entry_option_price": 9.65, "execution_mode": "option", "matched_signals": 38, "option_liquidity_status": "ok", "option_open_interest": 2308.0, "option_spread_pct": 3.81, "option_volume": 583.0, "success_rate": 84.21, "ticker": "TEAM", "timing_score": 0.669}
       2026-05-05T15:00:00-04:00     entry_1500 timing_overlay                                                                                                                                                                                                                                                                      {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-05", "training_samples": 5543, "window": 5}
2026-05-05T13:30:09.549744-04:00    manage_1330   slot_skipped                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-05-05T13:25:09.992302-04:00    manage_1330   slot_skipped                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-05-05T13:10:09.568185-04:00    manage_1300   slot_skipped                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-05-05T13:05:09.617226-04:00    manage_1300   slot_skipped                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260506110219)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260506110219)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260506110219)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260506110219)

</details>
