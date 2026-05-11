# Reversal 3.4.1 Live Paper Test

Latest checkpoint (ET): `2026-05-11 10:37:19 EDT`
Last processed slot: `manage_1030`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry permission: `10:00 AM-12:00 PM ET` 5-minute scans may enter one exceptional candidate only when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`; the one-new-entry-per-day limit still applies
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`; off-hours `5-minute` checkpoints continue mark-to-market updates for open positions, while any legacy share positions still held from older versions continue extended-hours take-profit and stop loss scans until flat
- Live exit ladder: `+15% / +15% / -10%`
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$35,353.50`
- Equity: `$35,353.50`
- Realized PnL: `$25,353.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-05-11)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
   CEG     option         option CEG260618C00290000      7          2026-05-11         2026-05-11         23.2        26.8 2520.0   15.517241 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  NXPI           80.56               36            0.70              1.45        294.13                87.07         0.699          pass              0.392             44.8                           0.294               23.56              1.918                                 ok            True                  False
  TEAM           81.82               11            5.25              3.37         90.16               114.36         0.608          pass              0.127              3.6                           0.164               25.38              3.263                                 ok            True                  False
  GOOG           83.33               18            1.60              4.46        395.14                37.66         0.571          pass              0.270             23.6                           0.190               12.10              1.421                                 ok            True                  False
    ZS           81.48               27            1.82              1.94        151.30                58.64         0.538          pass              0.259             17.6                           0.223               11.37              1.358                                 ok            True                  False
   WMT           83.33               12            1.45              1.32        129.86                19.38         0.531          pass              0.176              6.9                           0.179                0.94              0.144                                 ok            True                  False
  MRVL          100.00               34            0.66              0.78        169.79                55.66         0.530          pass              0.870             85.5                           0.732                6.83              0.836                                 ok            True                   True
  MDLZ           85.71               21            0.84              0.36         61.39                24.76         0.518          pass              0.479             67.1                           0.540                6.29              0.484                                 ok            True                  False
   ADI           81.82               33            0.57              1.65        415.81                36.03         0.512          pass              0.413             53.2                           0.395                5.50              0.753                                 ok            True                  False
  TMUS           86.49               37            0.51              0.69        193.33                36.59         0.510          pass              0.595             63.6                           0.713                5.41              0.286                                 ok            True                  False
  ADSK           93.75               16            1.77              3.02        243.20                39.96         0.510          pass              0.458              0.0                           0.261                2.19              0.480                                 ok            True                  False
  CHTR           86.36               22            1.97              2.14        153.94               119.48         0.788          pass              0.469             47.0                           0.694              -13.06             -1.186            downtrend_blocked_slope           False                  False
 CMCSA           88.46               26            0.51              0.09         25.36                62.19         0.682          pass              0.541             46.9                           0.406               -8.16             -0.813 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                                                                                                                                                                                                                                                                           detail
2026-05-11T10:37:19.097633-04:00 early_entry_1035 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-11T10:37:19.097633-04:00      manage_1030          exit                                                                                                                                                                                                                                             {"asset_type": "option", "contract_symbol": "CEG260618C00290000", "fill_price": 26.8, "pnl": 2520.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 15.52, "ticker": "CEG"}
2026-05-11T10:30:53.059924-04:00 early_entry_1030 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-11T10:24:36.025323-04:00 early_entry_1020 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-11T10:18:18.755092-04:00 early_entry_1015 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-11T10:12:01.604493-04:00 early_entry_1010 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-11T10:05:43.962541-04:00 early_entry_1005         entry {"allocated_cash": 16240.0, "asset_type": "option", "contract_symbol": "CEG260618C00290000", "contracts": 7, "early_entry_score": 0.766, "entry_mode": "early", "entry_option_price": 23.2, "execution_mode": "option", "matched_signals": 39, "option_liquidity_status": "ok", "option_open_interest": 991.0, "option_spread_pct": 14.66, "option_volume": 18.0, "success_rate": 89.74, "ticker": "CEG", "timing_score": 0.357}
2026-05-11T09:18:42.943466-04:00     data_refresh  data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                    {'saved': 92}
2026-05-08T16:05:06.142170-04:00      manage_1600          exit                                                                                                                                                                                                                                           {"asset_type": "option", "contract_symbol": "TEAM260618C00090000", "fill_price": 9.25, "pnl": 2850.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 19.35, "ticker": "TEAM"}
2026-05-08T16:00:06.094263-04:00      manage_1600  slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.1 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260511103719)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.1 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260511103719)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.1 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260511103719)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.1 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260511103719)

</details>
