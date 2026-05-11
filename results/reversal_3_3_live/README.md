# Reversal 3.4.1 Live Paper Test

Latest checkpoint (ET): `2026-05-11 10:24:36 EDT`
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

- Cash: `$16,593.50`
- Equity: `$34,233.50`
- Realized PnL: `$22,833.50`
- Unrealized PnL: `$1,400.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   CEG     option         option CEG260618C00290000       2026-05-11                   0      7     16240.0                 17640.0         23.2           25.2      301.86        302.04          1400.0                   8.62         89.74               39              0.58         46.89           52.76                  48.41                 991.0           18.0               0.15                      ok
```

## Today's Closed Trades (2026-05-11)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  TEAM           81.82               22            3.91              2.51         90.53               114.36         0.628          pass              0.230             12.8                           0.192               27.16              3.327                                 ok            True                  False
  GOOG           86.36               22            1.37              3.81        395.42                37.66         0.564          pass              0.410             34.8                           0.374               12.36              1.432                                 ok            True                  False
    ZS           83.33               36            1.09              1.16        151.63                58.64         0.536          pass              0.407             30.3                           0.264               12.20              1.392                                 ok            True                  False
  MRVL          100.00               29            1.16              1.38        169.54                55.66         0.531          pass              0.803             74.5                           0.851                6.29              0.813                                 ok            True                  False
   WMT           83.33               12            1.44              1.32        129.87                19.38         0.531          pass              0.177              7.4                           0.206                0.94              0.145                                 ok            True                  False
   ADP           93.55               31            0.51              0.76        212.67                34.95         0.518          pass              0.776             74.2                           0.597                7.44              0.501                                 ok            True                   True
  ORLY           84.00               25            1.19              0.77         92.63                35.12         0.518          pass              0.389             43.6                           0.657               -0.13              0.031                                 ok            True                  False
  TMUS           86.11               36            0.62              0.85        193.27                36.59         0.509          pass              0.554             55.5                           0.643                5.29              0.281                                 ok            True                  False
  ASML           84.62               13            3.28             36.57       1576.35                48.89         0.505          pass              0.222              9.4                           0.225                7.49              1.205                                 ok            True                  False
  CHTR           88.89               27            1.48              1.61        154.17               119.48         0.791          pass              0.610             60.2                           0.796              -12.63             -1.164            downtrend_blocked_slope           False                  False
  NXPI           78.79               33            0.98              2.02        293.88                87.07         0.699          pass              0.292             23.1                           0.165               23.22              1.906                                 ok           False                  False
 CMCSA           91.18               34            0.16              0.03         25.38                62.19         0.662          pass              0.775             83.7                           0.626               -7.83             -0.797 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                                                                                                                                                                                                                                                                           detail
2026-05-11T10:24:36.025323-04:00 early_entry_1020 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-11T10:18:18.755092-04:00 early_entry_1015 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-11T10:12:01.604493-04:00 early_entry_1010 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-11T10:05:43.962541-04:00 early_entry_1005         entry {"allocated_cash": 16240.0, "asset_type": "option", "contract_symbol": "CEG260618C00290000", "contracts": 7, "early_entry_score": 0.766, "entry_mode": "early", "entry_option_price": 23.2, "execution_mode": "option", "matched_signals": 39, "option_liquidity_status": "ok", "option_open_interest": 991.0, "option_spread_pct": 14.66, "option_volume": 18.0, "success_rate": 89.74, "ticker": "CEG", "timing_score": 0.357}
2026-05-11T09:18:42.943466-04:00     data_refresh  data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                    {'saved': 92}
2026-05-08T16:05:06.142170-04:00      manage_1600          exit                                                                                                                                                                                                                                           {"asset_type": "option", "contract_symbol": "TEAM260618C00090000", "fill_price": 9.25, "pnl": 2850.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 19.35, "ticker": "TEAM"}
2026-05-08T16:00:06.094263-04:00      manage_1600  slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "already_processed"}
2026-05-08T15:55:02.084715-04:00      manage_1600  slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "already_processed"}
2026-05-08T15:40:02.063692-04:00      manage_1530  slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "already_processed"}
2026-05-08T15:35:05.923584-04:00      manage_1530  slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.1 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260511102436)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.1 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260511102436)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.1 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260511102436)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.1 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260511102436)

</details>
