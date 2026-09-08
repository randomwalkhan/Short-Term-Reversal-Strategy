# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-08 10:10:03 EDT`
Last processed slot: `manage_1000`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO + DRAM`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry mode: `shadow-only`; `10:00 AM-12:00 PM ET` 5-minute scans still log candidates when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`, but they do not open positions
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`; off-hours `5-minute` checkpoints continue mark-to-market updates for open positions, while any legacy share positions still held from older versions continue extended-hours take-profit and stop loss scans until flat
- Live exit ladder: `+15% / +15% / -10%`
- Option entry liquidity gate: `open interest >= 110`, `volume >= 20`, `spread <= 14%`
- Option exit safety: stale option `lastPrice` may be shown for mark-to-market, but take-profit / stop-loss triggers require an executable quote from bid/ask or bid
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$77,148.10`
- Equity: `$77,148.10`
- Realized PnL: `$67,148.10`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-08)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  MSTR     option         option MSTR261016C00145000     30          2026-09-04         2026-09-08       13.375     12.0375 -4012.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  CRWD           82.35               17            3.07              4.58        211.14                91.63         0.634          pass              0.217             14.8                           0.142                8.32              0.998                                 ok            True                  False
   KHC          100.00               12            0.58              0.10         24.81                29.15         0.623          pass              0.694             72.6                           0.746               -2.22              0.042                                 ok            True                  False
   WMT           85.00               20            1.15              0.86        106.77                40.24         0.592          pass              0.262              0.8                           0.186               -0.54              0.225                                 ok            True                  False
  MELI          100.00               30            0.94             12.96       1972.80                45.80         0.567          pass              0.775             61.7                           0.739                0.61              0.119                                 ok            True                   True
  NVDA           90.91               33            0.72              1.16        229.86                44.80         0.538          pass              0.582             28.0                           0.174                9.70              0.910                                 ok            True                  False
  CPRT           86.67               15            2.39              0.56         33.48                42.28         0.532          pass              0.296             10.6                           0.202               -1.04              0.022                                 ok            True                  False
  REGN          100.00               13            1.45              8.39        824.12                29.02         0.525          pass              0.645             57.6                           0.703               -1.54              0.129                                 ok            True                  False
  CHTR           92.31               26            2.11              2.24        151.03                60.37         0.522          pass              0.558             23.8                           0.231               -1.00             -0.084                                 ok            True                  False
  UPRO           87.50               16            1.57              1.67        151.17                24.27         0.519          pass              0.303              3.6                           0.197                0.62              0.069                                 ok            True                  False
  CSCO           86.84               38            0.51              0.39        109.03                36.41         0.513          pass              0.491             23.4                           0.211               -1.44             -0.267                                 ok            True                  False
  MSFT           88.24               17            1.59              5.56        497.32                23.39         0.502          pass              0.336              6.6                           0.158                0.91              0.122                                 ok            True                  False
  PYPL           90.00               10            1.97              0.76         54.64                57.43         0.644          pass              0.422             30.3                           0.532              -12.43             -1.513 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         detail
2026-09-08T10:10:03.508736-04:00 early_entry_1010 early_entry_shadow    {"contract_symbol": "INSM261016C00125000", "current_drop_pct": 0.56, "early_entry_score": 0.785, "early_reclaim_pct": 85.6, "entry_ask": 7.9, "entry_bid": 4.9, "entry_mode": "early", "entry_option_price": 6.4, "hypothetical_budget": 38574.05, "hypothetical_contracts": 60, "matched_signals": 43, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 70.0, "option_spread_pct": 46.88, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.851, "shadow_only": true, "success_rate": 90.7, "ticker": "INSM", "timing_score": 0.426, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.785, "early_reclaim_pct": 85.6, "matched_signals": 43, "recovery_stability_score": 0.851, "success_rate": 90.7, "ticker": "INSM", "timing_score": 0.426, "trend_health_status": "ok"}, {"current_drop_pct": 0.94, "early_entry_score": 0.775, "early_reclaim_pct": 61.7, "matched_signals": 30, "recovery_stability_score": 0.739, "success_rate": 100.0, "ticker": "MELI", "timing_score": 0.567, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-08T10:05:01.504433-04:00 early_entry_1005 early_entry_shadow {"contract_symbol": "MELI261023C01970000", "current_drop_pct": 0.58, "early_entry_score": 0.839, "early_reclaim_pct": 76.1, "entry_ask": 104.9, "entry_bid": 84.2, "entry_mode": "early", "entry_option_price": 94.55, "hypothetical_budget": 38574.05, "hypothetical_contracts": 4, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 1.0, "option_spread_pct": 21.89, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.768, "shadow_only": true, "success_rate": 100.0, "ticker": "MELI", "timing_score": 0.57, "top_candidates": [{"current_drop_pct": 0.58, "early_entry_score": 0.839, "early_reclaim_pct": 76.1, "matched_signals": 33, "recovery_stability_score": 0.768, "success_rate": 100.0, "ticker": "MELI", "timing_score": 0.57, "trend_health_status": "ok"}, {"current_drop_pct": 0.55, "early_entry_score": 0.796, "early_reclaim_pct": 85.9, "matched_signals": 45, "recovery_stability_score": 0.846, "success_rate": 91.11, "ticker": "INSM", "timing_score": 0.416, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-08T10:00:06.216987-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-08T09:50:04.503186-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"asset_type": "option", "contract_symbol": "MSTR261016C00145000", "fill_price": 12.0375, "pnl": -4012.5, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "MSTR"}
2026-09-08T00:00:05.865092-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {'saved': 93}
2026-09-07T23:55:04.287626-04:00   share_ext_2355      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"holiday_name": "Labor Day", "reason": "nyse_holiday"}
2026-09-07T23:50:01.089933-04:00   share_ext_2350      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"holiday_name": "Labor Day", "reason": "nyse_holiday"}
2026-09-07T23:45:01.091566-04:00   share_ext_2345      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"holiday_name": "Labor Day", "reason": "nyse_holiday"}
2026-09-07T23:40:05.520694-04:00   share_ext_2340      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"holiday_name": "Labor Day", "reason": "nyse_holiday"}
2026-09-07T23:35:01.092604-04:00   share_ext_2335      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"holiday_name": "Labor Day", "reason": "nyse_holiday"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260908101003)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260908101003)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260908101003)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260908101003)

</details>
