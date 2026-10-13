# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-13 10:25:06 EDT`
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

- Cash: `$75,459.30`
- Equity: `$138,079.30`
- Realized PnL: `$123,274.30`
- Unrealized PnL: `$4,805.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   CEG     option         option CEG261120C00290000       2026-10-12                   1     31     57815.0                 62620.0        18.65           20.2      291.07        294.82          bid_ask_mid                       20.2                bid_ask_mid                    True          4805.0                   8.31         83.33               12              2.35         48.77           49.35                  62.49                 920.0          121.0               0.05                      ok
```

## Today's Closed Trades (2026-10-13)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct                  exit_reason
  CTSH     option         option CTSH261120C00060000    160          2026-10-09         2026-10-13         3.65        4.65 16000.0    27.39726 take_profit_day2_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MDLZ           95.00               20            0.50              0.22         61.70                19.83         0.543            pass              0.627             35.4                           0.294                4.56              0.656                                 ok            True                  False
  CSCO           91.67               24            0.71              0.57        115.09                34.19         0.537            pass              0.663             68.2                           0.437                7.50              0.916                                 ok            True                  False
  SNPS           86.84               38            0.57              2.00        501.65                52.43         0.536            pass              0.658             78.6                           0.471               20.37              1.529                                 ok            True                  False
  ISRG           91.67               12            1.93              5.78        425.16                25.00         0.507            pass              0.455             26.8                           0.287                1.75              0.536                                 ok            True                  False
  INTC           88.89               36            1.02              0.72        101.04                67.41         0.572            pass              0.669             67.0                           0.678              -13.47             -1.872 downtrend_blocked_slope_and_streak           False                  False
  MPWR           86.36               22            1.70             15.71       1312.50                51.39         0.550            pass              0.413             35.9                           0.321               -4.23             -0.347            downtrend_blocked_slope           False                  False
   KDP           96.30               27            0.40              0.09         32.71                30.00         0.542            pass              0.718             50.0                           0.451                5.12              0.641                                 ok           False                  False
   XEL           86.96               23            0.38              0.20         74.09                18.13         0.511            pass              0.522             66.1                           0.583                4.53              0.570                                 ok           False                  False
  SHOP           85.37               41            0.37              0.46        179.02                48.43         0.509            pass              0.657             87.8                           0.712               20.44              2.090                                 ok           False                  False
  UPRO           83.78               37            0.18              0.20        155.37                28.94         0.507            pass              0.542             70.0                           0.389                4.88              0.598                                 ok           False                  False
   PEP           78.26               23            0.42              0.37        126.52                21.61         0.506            pass              0.252             38.4                           0.287               -1.97             -0.063                                 ok           False                  False
  DASH           88.10               42            0.28              0.38        194.08                43.05         0.493 below_threshold              0.684             72.9                           0.461                3.53              0.592                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                 detail
2026-10-13T10:25:06.600262-04:00 early_entry_1025 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-13T10:20:06.700982-04:00 early_entry_1020 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-13T10:15:06.623973-04:00 early_entry_1015 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-13T10:10:05.811238-04:00 early_entry_1010 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-13T10:05:05.477631-04:00 early_entry_1005 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-13T10:00:05.694425-04:00 early_entry_1000 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-13T09:50:04.590337-04:00      manage_1000               exit {"asset_type": "option", "contract_symbol": "CTSH261120C00060000", "fill_price": 4.65, "pnl": 16000.0, "reason": "take_profit_day2_hit_at_scan", "return_pct": 27.4, "ticker": "CTSH"}
2026-10-13T00:00:05.318337-04:00     data_refresh       data_refresh                                                                                                                                                              {'saved': 91, 'empty': 2}
2026-10-12T15:10:05.555878-04:00       entry_1500       slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-10-12T15:05:06.325460-04:00       entry_1500       slot_skipped                                                                                                                                                        {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261013102506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261013102506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261013102506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261013102506)

</details>
