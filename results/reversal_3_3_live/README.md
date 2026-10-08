# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-08 09:40:06 EDT`
Last processed slot: `manage_0930`

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

- Cash: `$734.30`
- Equity: `$108,109.30`
- Realized PnL: `$95,146.80`
- Unrealized PnL: `$2,962.50`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  ABNB     option         option ABNB261120C00160000       2026-10-06                   2     55     52112.5                 54175.0         9.48           9.85      160.14        162.79     last_price_stale                        NaN                unavailable                   False          2062.5                   3.96         83.33               12              2.40         42.26             0.0                  40.56                 310.0           20.0               0.06                      ok
  NVDA     option         option NVDA261120C00235000       2026-10-07                   1     40     52300.0                 53200.0        13.08          13.30      236.83        234.52     last_price_stale                        NaN                unavailable                   False           900.0                   1.72         90.91               22              1.01         37.07             0.2                  24.15               17037.0         1205.0               0.01                      ok
```

## Today's Closed Trades (2026-10-08)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MPWR           88.00               25            1.56             15.62       1419.29                55.22         0.579          pass              0.466             31.6                           0.344                5.26              0.853                                 ok            True                  False
   ADI           87.50               24            1.24              3.56        408.56                34.70         0.521          pass              0.464             39.5                           0.420                5.85              0.714                                 ok            True                  False
  UPRO           83.33               24            1.05              1.14        154.73                30.53         0.516          pass              0.363             43.2                           0.516                2.40              0.410                                 ok            True                  False
  AVGO           85.00               20            1.90              5.01        374.36                34.55         0.504          pass              0.296             15.4                           0.265                5.42              0.721                                 ok            True                  False
  QCOM           87.50               24            1.48              1.83        176.33                56.66         0.599          pass              0.456             34.3                           0.423              -10.17             -1.089 downtrend_blocked_slope_and_streak           False                  False
  MSTR           88.89               18            3.45              3.70        151.78                80.80         0.589          pass              0.358              2.8                           0.179               -8.37             -0.242           downtrend_blocked_streak           False                  False
  CSCO           89.29               28            0.38              0.31        117.26                34.80         0.565          pass              0.626             67.4                           0.703                9.74              1.212                                 ok           False                  False
   CEG           86.84               38            0.36              0.76        299.27                58.54         0.564          pass              0.668             80.7                           0.647               14.10              1.492                                 ok           False                  False
  META           83.78               37            0.33              1.66        720.60                52.76         0.560          pass              0.574             78.9                           0.462               -7.54             -0.408            downtrend_blocked_slope           False                  False
   STX           89.66               29            2.08             11.75        802.53                69.74         0.550          pass              0.482             14.2                           0.265              -12.71             -1.574            downtrend_blocked_slope           False                  False
   WDC           80.00               30            1.77              5.02        403.27                65.89         0.538          pass              0.216              9.5                           0.292              -11.56             -1.389            downtrend_blocked_slope           False                  False
  AMGN           78.57               14            1.36              3.93        411.40                28.61         0.538          pass              0.086              1.9                           0.063                0.35             -0.232                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                     detail
2026-10-08T00:00:04.872922-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                  {'saved': 91, 'empty': 2}
2026-10-07T15:10:05.672351-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-10-07T15:05:05.765684-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-10-07T15:00:04.880221-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-10-07T14:55:05.726912-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-10-07T14:50:06.730595-04:00       entry_1500                   entry {"allocated_cash": 52300.0, "asset_type": "option", "contract_symbol": "NVDA261120C00235000", "contracts": 40, "early_entry_score": 0.461, "entry_mode": "regular", "entry_option_price": 13.075, "execution_mode": "option", "matched_signals": 22, "option_liquidity_status": "ok", "option_open_interest": 17037.0, "option_spread_pct": 1.15, "option_volume": 1205.0, "success_rate": 90.91, "ticker": "NVDA", "timing_score": 0.512}
2026-10-07T14:50:06.730595-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                 {"early_entry_score": 0.14, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 17.0, "option_spread_pct": 11.88, "option_volume": 2.0, "reason": "no_trade_low_option_liquidity", "ticker": "MPWR", "timing_score": 0.522}
2026-10-07T14:50:06.730595-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                   {"early_entry_score": 0.49, "option_liquidity_status": "low_volume", "option_open_interest": 993.0, "option_spread_pct": 12.24, "option_volume": 2.0, "reason": "no_trade_low_option_liquidity", "ticker": "KDP", "timing_score": 0.545}
2026-10-07T14:50:06.730595-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                               {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-10-07", "training_samples": 5970, "window": 5}
2026-10-07T12:00:04.521112-04:00 early_entry_1200      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261008094006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261008094006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261008094006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261008094006)

</details>
