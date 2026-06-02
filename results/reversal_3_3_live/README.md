# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-02 10:20:01 EDT`
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
- Option entry liquidity gate: `open interest >= 110`, `volume >= 20`, `spread <= 14%`
- Option exit safety: stale option `lastPrice` may be shown for mark-to-market, but take-profit / stop-loss triggers require an executable quote from bid/ask or bid
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$33,669.25`
- Equity: `$33,669.25`
- Realized PnL: `$23,669.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-06-02)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  FTNT          100.00               19            1.74              1.79        146.37                71.69         0.661          pass              0.705             59.5                           0.752               14.29              1.248                                 ok            True                  False
  MNST           95.00               20            1.36              0.85         88.74                49.60         0.628          pass              0.571             14.0                           0.183               -0.74              0.178                                 ok            True                  False
  MELI           92.31               26            1.59             19.25       1722.73                60.28         0.602          pass              0.633             46.1                           0.590                7.41              0.732                                 ok            True                  False
  AMGN           90.00               10            1.24              2.85        327.91                20.27         0.560          pass              0.444             40.4                           0.467                0.21              0.020                                 ok            True                  False
  INSM           50.00               12            4.03              2.99        104.75               110.78         0.669          pass              0.146             21.9                           0.427               -5.03             -0.325            downtrend_blocked_slope           False                  False
   WMT           76.92               13            1.41              1.13        114.11                32.65         0.570          pass              0.096              6.4                           0.099              -15.27             -1.712 downtrend_blocked_slope_and_streak           False                  False
  SHOP           72.73               11            4.14              3.60        122.58                84.68         0.555          pass              0.127             21.5                           0.412               16.20              1.966                                 ok           False                  False
    ZS           50.00                4            8.09              8.82        151.93               157.27         0.555          pass              0.101             15.0                           0.401              -18.08             -2.773            downtrend_blocked_slope           False                  False
  REGN           86.67               30            0.81              3.43        599.19                42.53         0.550          pass              0.505             46.4                           0.489               -5.24             -0.642 downtrend_blocked_slope_and_streak           False                  False
  MSFT          100.00                2            2.84              9.16        456.59                28.37         0.547          pass              0.524             23.1                           0.458                5.87              0.834                                 ok           False                  False
   HON           78.57               14            1.07              1.77        235.78                24.20         0.541          pass              0.144             21.2                           0.179                7.72              0.982                                 ok           False                  False
  UPRO           94.44               36            0.08              0.08        150.26                29.00         0.527          pass              0.893             93.9                           0.828                7.76              0.943                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                 detail
2026-06-02T10:20:01.327977-04:00 early_entry_1020           entry_skipped                                                                                                                                                                                                                             {"reason": "no_candidate"}
2026-06-02T10:15:02.269482-04:00 early_entry_1015           entry_skipped                                                                                                                                                                                                 {"reason": "no_trade_after_option_and_timing_filters"}
2026-06-02T10:15:02.269482-04:00 early_entry_1015 entry_candidate_skipped {"early_entry_score": 0.679, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 117.0, "option_spread_pct": 24.24, "option_volume": 5.0, "reason": "no_trade_low_option_liquidity", "ticker": "CHTR", "timing_score": 0.442}
2026-06-02T10:10:06.260122-04:00 early_entry_1010           entry_skipped                                                                                                                                                                                                                             {"reason": "no_candidate"}
2026-06-02T10:05:01.451088-04:00 early_entry_1005           entry_skipped                                                                                                                                                                                                                             {"reason": "no_candidate"}
2026-06-02T10:00:02.499087-04:00 early_entry_1000           entry_skipped                                                                                                                                                                                                                             {"reason": "no_candidate"}
2026-06-02T09:20:05.650957-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                          {'saved': 92}
2026-06-01T15:10:04.135705-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-06-01T15:05:05.129733-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-06-01T15:00:02.274373-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                        {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260602102001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260602102001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260602102001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260602102001)

</details>
