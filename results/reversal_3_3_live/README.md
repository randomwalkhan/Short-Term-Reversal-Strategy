# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-21 14:40:07 EDT`
Last processed slot: `manage_1430`

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
- Option entry liquidity gate: `open interest >= 110`, `volume >= 20`, `spread <= 14%`
- Option exit safety: stale option `lastPrice` may be shown for mark-to-market, but take-profit / stop-loss triggers require an executable quote from bid/ask or bid
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$16,177.75`
- Equity: `$28,377.75`
- Realized PnL: `$18,317.75`
- Unrealized PnL: `$60.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  AVGO     option         option AVGO260717C00420000       2026-05-21                   0      4     12140.0                 12200.0        30.35           30.5      415.18        413.27          bid_ask_mid                       30.5                bid_ask_mid                    True            60.0                   0.49         91.67               36              0.62         50.17           51.05                  40.33                2101.0          296.0               0.03                      ok
```

## Today's Closed Trades (2026-05-21)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  FTNT          100.00               28            1.22              1.11        129.53                70.74         0.649          pass              0.713             42.8                           0.409               18.94              1.768                                 ok            True                  False
  MNST           84.85               33            0.67              0.41         86.71                49.77         0.539          pass              0.598             87.0                           0.715               13.60              0.670                                 ok            True                  False
  NVDA           85.71               21            1.57              2.45        222.42                44.60         0.530          pass              0.389             36.8                           0.260                4.00              0.341                                 ok            True                  False
    ZS           83.33               18            2.34              2.86        173.23                63.59         0.522          pass              0.274             26.6                           0.406               11.51              1.812                                 ok            True                  False
  AVGO           93.55               31            1.11              3.24        416.37                40.33         0.502          pass              0.653             33.9                           0.250                0.14             -0.187                                 ok            True                  False
  INTC           97.50               40            0.12              0.10        118.92               113.85         0.733          pass              0.966             97.5                           0.763                8.39             -0.525                                 ok           False                  False
  NXPI           73.33               15            2.92              6.35        307.43                91.65         0.664          pass              0.185             28.5                           0.386                3.74              0.209                                 ok           False                  False
  SBUX          100.00                8            1.76              1.31        105.94                31.64         0.607          pass              0.565             34.9                           0.437                0.94              0.174                                 ok           False                  False
  REGN           91.67               24            1.17              5.32        647.48                50.54         0.598          pass              0.535             23.6                           0.210               -9.30             -1.401 downtrend_blocked_slope_and_streak           False                  False
  PAYX           95.00               20            0.46              0.30         94.79                29.35         0.562          pass              0.762             79.9                           0.660                1.53              0.260                                 ok           False                  False
  TEAM           87.50               16            4.78              2.88         84.99               114.20         0.545          pass              0.358             21.1                           0.170              -11.11             -0.610 downtrend_blocked_slope_and_streak           False                  False
  MPWR           90.32               31            0.74              8.04       1549.82                57.81         0.544          pass              0.677             69.2                           0.649               -2.17             -0.737 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-05-21T12:00:02.068266-04:00 early_entry_1200           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-21T11:55:01.035616-04:00 early_entry_1155           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-21T11:50:01.038543-04:00 early_entry_1150                   entry {"allocated_cash": 12140.0, "asset_type": "option", "contract_symbol": "AVGO260717C00420000", "contracts": 4, "early_entry_score": 0.724, "entry_mode": "early", "entry_option_price": 30.35, "execution_mode": "option", "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 2101.0, "option_spread_pct": 2.97, "option_volume": 296.0, "success_rate": 91.67, "ticker": "AVGO", "timing_score": 0.497}
2026-05-21T11:45:04.222670-04:00 early_entry_1145           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate"}
2026-05-21T11:40:04.207622-04:00 early_entry_1140           entry_skipped                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-21T11:40:04.207622-04:00 early_entry_1140 entry_candidate_skipped                                                                                                                                                                            {"early_entry_score": 0.775, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 29.0, "option_spread_pct": 7.04, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "ADP", "timing_score": 0.527}
2026-05-21T11:35:02.090762-04:00 early_entry_1135           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate"}
2026-05-21T11:30:02.245220-04:00 early_entry_1130           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate"}
2026-05-21T11:25:04.201711-04:00 early_entry_1125           entry_skipped                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-21T11:25:04.201711-04:00 early_entry_1125 entry_candidate_skipped                                                                                                                                                                            {"early_entry_score": 0.804, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 29.0, "option_spread_pct": 6.12, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "ADP", "timing_score": 0.527}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260521144007)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260521144007)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260521144007)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260521144007)

</details>
