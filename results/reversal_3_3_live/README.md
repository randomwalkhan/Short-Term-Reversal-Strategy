# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-21 14:05:07 EDT`
Last processed slot: `manage_1400`

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
- Equity: `$28,507.75`
- Realized PnL: `$18,317.75`
- Unrealized PnL: `$190.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  AVGO     option         option AVGO260717C00420000       2026-05-21                   0      4     12140.0                 12330.0        30.35          30.82      415.18        414.35          bid_ask_mid                      30.82                bid_ask_mid                    True           190.0                   1.57         91.67               36              0.62         50.17            50.6                  40.33                2101.0          296.0               0.03                      ok
```

## Today's Closed Trades (2026-05-21)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  FTNT          100.00               32            1.10              1.00        129.57                70.74         0.631          pass              0.754             48.2                           0.637               19.08              1.773                                 ok            True                  False
  PAYX           94.44               18            0.67              0.45         94.73                29.35         0.561          pass              0.706             70.4                           0.603                1.31              0.250                                 ok            True                  False
  MNST           83.87               31            0.69              0.42         86.70                49.77         0.550          pass              0.558             86.5                           0.715               13.57              0.669                                 ok            True                  False
  NVDA           89.29               28            1.01              1.58        222.79                44.60         0.523          pass              0.598             59.2                           0.481                4.59              0.366                                 ok            True                  False
    ZS           82.35               17            2.56              3.13        173.11                63.59         0.514          pass              0.220             19.6                           0.392               11.25              1.801                                 ok            True                  False
  ISRG           90.00               20            1.68              5.27        446.77                35.82         0.508          pass              0.521             45.7                           0.688               -2.65              0.016                                 ok            True                  False
  INTC           97.44               39            0.24              0.20        118.87               113.85         0.732          pass              0.952             95.0                           0.780                8.26             -0.531                                 ok           False                  False
  NXPI           73.33               15            2.76              5.98        307.59                91.65         0.674          pass              0.198             32.5                           0.511                3.92              0.216                                 ok           False                  False
   TRI           73.33               15            1.10              0.66         85.08                55.83         0.604          pass              0.281             62.5                           0.679               -8.90             -0.700 downtrend_blocked_slope_and_streak           False                  False
  SBUX          100.00                5            2.16              1.61        105.81                31.64         0.603          pass              0.520             20.0                           0.353                0.52              0.155                                 ok           False                  False
  REGN           92.31               26            1.13              5.16        647.55                50.54         0.588          pass              0.571             25.9                           0.355               -9.27             -1.400 downtrend_blocked_slope_and_streak           False                  False
  TEAM           86.96               23            3.83              2.31         85.24               114.20         0.557          pass              0.438             36.7                           0.607              -10.23             -0.565 downtrend_blocked_slope_and_streak           False                  False
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

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260521140507)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260521140507)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260521140507)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260521140507)

</details>
