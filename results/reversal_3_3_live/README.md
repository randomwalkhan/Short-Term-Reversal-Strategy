# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-05-06 09:53:26 EDT`
Last processed slot: `manage_1000`

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

- Cash: `$12,472.50`
- Equity: `$24,022.50`
- Realized PnL: `$13,087.50`
- Unrealized PnL: `$935.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  TEAM     option         option TEAM260618C00090000       2026-05-05                   1     11     10615.0                 11550.0         9.65           10.5       91.46         84.93           935.0                   8.81         84.21               38              1.82         72.84            3.13                 121.39                2308.0          583.0               0.04                      ok
```

## Today's Closed Trades (2026-05-06)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  CDNS           97.30               37            0.61              1.50        352.99                54.11            True
   XEL           93.33               15            1.07              0.61         81.19                28.13            True
  FTNT           88.89               18            1.80              1.13         89.43                40.66            True
  PANW           80.77               26            1.30              1.68        183.26                45.58            True
  ADSK           81.82               11            2.98              5.20        247.20                46.09            True
    ZS           80.00               15            3.61              3.57        139.83                69.30            True
  ADBE           84.00               25            1.98              3.55        254.10                46.79            True
  MSTR           87.80               41            0.90              1.18        186.40                66.92            True
  PLTR           85.19               27            1.86              1.77        135.15                62.37            True
  DDOG           89.29               28            1.72              1.75        144.98                55.69            True
  COST           89.47               19            0.93              6.60       1013.59                18.81            True
  CHTR           90.48               42            0.49              0.55        158.00               118.74           False
```

## Recent Events

```text
                    timestamp_et           slot     event_type                                                                                                                                                                                                                                                                                                                                                                            detail
2026-05-06T09:35:01.127893-04:00    manage_0930   slot_skipped                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-05-06T00:00:03.652066-04:00   data_refresh   data_refresh                                                                                                                                                                                                                                                                                                                                                                     {'saved': 99}
       2026-05-05T16:01:00-04:00 backfill_audit backfill_audit                                                                                                               {"open_positions_after_backfill": 1, "reason": "Mac was offline; reconstructed missed 2026-05-05 ET afternoon slots using stock and option 1m bars clipped at each slot time", "slots": ["manage_1400", "manage_1430", "entry_1500", "manage_1530", "manage_1600"]}
       2026-05-05T15:00:00-04:00     entry_1500          entry {"allocated_cash": 10615.0, "asset_type": "option", "contract_symbol": "TEAM260618C00090000", "contracts": 11, "entry_option_price": 9.65, "execution_mode": "option", "matched_signals": 38, "option_liquidity_status": "ok", "option_open_interest": 2308.0, "option_spread_pct": 3.81, "option_volume": 583.0, "success_rate": 84.21, "ticker": "TEAM", "timing_score": 0.669}
       2026-05-05T15:00:00-04:00     entry_1500 timing_overlay                                                                                                                                                                                                                                                                      {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-05", "training_samples": 5543, "window": 5}
2026-05-05T13:30:09.549744-04:00    manage_1330   slot_skipped                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-05-05T13:25:09.992302-04:00    manage_1330   slot_skipped                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-05-05T13:10:09.568185-04:00    manage_1300   slot_skipped                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-05-05T13:05:09.617226-04:00    manage_1300   slot_skipped                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-05-05T13:00:07.034754-04:00    manage_1300   slot_skipped                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260506095326)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260506095326)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260506095326)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260506095326)

</details>
