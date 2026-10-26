# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-26 10:35:02 EDT`
Last processed slot: `manage_1030`

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

- Cash: `$65,421.80`
- Equity: `$142,619.30`
- Realized PnL: `$127,691.80`
- Unrealized PnL: `$4,927.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   EXC     option         option EXC261218C00045000       2026-10-23                   1    657     72270.0                 77197.5          1.1           1.18       44.42         44.54          bid_ask_mid                       1.18                bid_ask_mid                    True          4927.5                   6.82          80.0               15              0.97         20.09            25.0                  20.91                 278.0           48.0               0.09                      ok
```

## Today's Closed Trades (2026-10-26)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  TEAM     option         option TEAM261120C00230000     40          2026-10-22         2026-10-26        17.85      16.065 -7140.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  CTSH           94.44               36            0.75              0.37         70.38                46.28         0.511            pass              0.754             48.0                           0.376               17.31              1.817                                 ok            True                  False
  TMUS           82.14               28            0.71              0.73        146.23                64.13         0.642            pass              0.422             60.3                           0.423               -4.19             -0.398            downtrend_blocked_slope           False                  False
   CEG           88.24               34            0.83              1.47        252.82                65.46         0.605            pass              0.591             50.5                           0.455              -14.48             -1.592 downtrend_blocked_slope_and_streak           False                  False
  MDLZ           87.50                8            1.04              0.47         63.60                25.23         0.594            pass              0.316             18.9                           0.229                2.18              0.336                                 ok           False                  False
   STX           76.19               42            0.13              0.59        630.24                71.81         0.578            pass              0.529             90.4                           0.591              -16.41             -1.654 downtrend_blocked_slope_and_streak           False                  False
  MRVL           89.74               39            0.47              0.75        228.19                64.81         0.546            pass              0.741             77.6                           0.657              -14.45             -1.478            downtrend_blocked_slope           False                  False
   KDP           96.88               32            0.17              0.04         34.66                26.07         0.524            pass              0.830             76.9                           0.446                5.71              0.652                                 ok           False                  False
   KHC           92.11               38            0.02              0.00         24.80                34.81         0.521            pass              0.853             97.1                           0.503               10.45              1.113                                 ok           False                  False
 CMCSA           75.00                4            1.83              0.29         22.57                23.68         0.512            pass              0.156             35.0                           0.471                7.71              0.907                                 ok           False                  False
  NFLX           76.00               25            1.23              0.57         65.61                35.37         0.492 below_threshold              0.204             18.2                           0.267               -7.89             -0.983 downtrend_blocked_slope_and_streak           False                  False
  TEAM          100.00               32            1.36              2.17        226.68                47.89         0.490 below_threshold              0.775             59.8                           0.790                8.07              1.041                                 ok           False                  False
  INTU           89.47               38            0.31              0.74        343.07                39.39         0.487 below_threshold              0.726             79.3                           0.494               11.88              1.406                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-10-26T10:35:02.828763-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-26T10:30:05.918649-04:00 early_entry_1030 early_entry_shadow {"contract_symbol": "TEAM261127C00225000", "current_drop_pct": 1.07, "early_entry_score": 0.821, "early_reclaim_pct": 68.5, "entry_ask": 21.3, "entry_bid": 17.8, "entry_mode": "early", "entry_option_price": 19.55, "hypothetical_budget": 32710.9, "hypothetical_contracts": 16, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 5.0, "option_spread_pct": 17.9, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.854, "shadow_only": true, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.489, "top_candidates": [{"current_drop_pct": 1.07, "early_entry_score": 0.821, "early_reclaim_pct": 68.5, "matched_signals": 35, "recovery_stability_score": 0.854, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.489, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-26T10:25:07.004993-04:00 early_entry_1025 early_entry_shadow  {"contract_symbol": "TEAM261127C00225000", "current_drop_pct": 1.05, "early_entry_score": 0.823, "early_reclaim_pct": 69.0, "entry_ask": 21.1, "entry_bid": 17.8, "entry_mode": "early", "entry_option_price": 19.45, "hypothetical_budget": 32710.9, "hypothetical_contracts": 16, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 5.0, "option_spread_pct": 16.97, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.811, "shadow_only": true, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.49, "top_candidates": [{"current_drop_pct": 1.05, "early_entry_score": 0.823, "early_reclaim_pct": 69.0, "matched_signals": 35, "recovery_stability_score": 0.811, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.49, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-26T10:20:05.900511-04:00 early_entry_1020 early_entry_shadow                                              {"contract_symbol": "TTWO261218C00195000", "current_drop_pct": 0.59, "early_entry_score": 0.772, "early_reclaim_pct": 68.3, "entry_ask": 20.8, "entry_bid": 18.6, "entry_mode": "early", "entry_option_price": 19.7, "hypothetical_budget": 32710.9, "hypothetical_contracts": 16, "matched_signals": 39, "option_liquidity_status": "ok", "option_open_interest": 555.0, "option_spread_pct": 11.17, "option_volume": 802.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.685, "shadow_only": true, "success_rate": 92.31, "ticker": "TTWO", "timing_score": 0.454, "top_candidates": [{"current_drop_pct": 0.59, "early_entry_score": 0.772, "early_reclaim_pct": 68.3, "matched_signals": 39, "recovery_stability_score": 0.685, "success_rate": 92.31, "ticker": "TTWO", "timing_score": 0.454, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-26T10:20:05.900511-04:00      manage_1030               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"asset_type": "option", "contract_symbol": "TEAM261120C00230000", "fill_price": 16.065, "pnl": -7140.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "TEAM"}
2026-10-26T10:15:06.813436-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-26T10:10:04.818104-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-26T10:05:04.929222-04:00 early_entry_1005 early_entry_shadow                 {"contract_symbol": "ABNB261218C00170000", "current_drop_pct": 0.64, "early_entry_score": 0.705, "early_reclaim_pct": 62.5, "entry_ask": 12.55, "entry_bid": 10.05, "entry_mode": "early", "entry_option_price": 11.3, "hypothetical_budget": 1161.8, "hypothetical_contracts": 1, "matched_signals": 35, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 540.0, "option_spread_pct": 22.12, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.623, "shadow_only": true, "success_rate": 91.43, "ticker": "ABNB", "timing_score": 0.462, "top_candidates": [{"current_drop_pct": 0.64, "early_entry_score": 0.705, "early_reclaim_pct": 62.5, "matched_signals": 35, "recovery_stability_score": 0.623, "success_rate": 91.43, "ticker": "ABNB", "timing_score": 0.462, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-26T10:00:02.755892-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-26T03:00:06.095406-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {'saved': 91, 'empty': 2}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261026103502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261026103502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261026103502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261026103502)

</details>
