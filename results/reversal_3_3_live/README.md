# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-02 10:35:04 EDT`
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
    MU           82.35               34            0.57              4.11       1032.98               101.73         0.732          pass              0.506             69.9                           0.371               50.96              4.615                                 ok            True                  False
  FTNT          100.00               14            1.96              2.02        146.28                71.69         0.679          pass              0.658             54.4                           0.728               14.04              1.238                                 ok            True                  False
  MNST           92.31               13            1.62              1.01         88.67                49.60         0.652          pass              0.452             12.7                           0.216               -0.99              0.166                                 ok            True                  False
  MELI           89.47               19            2.04             24.68       1720.40                60.28         0.616          pass              0.467             30.8                           0.453                6.92              0.711                                 ok            True                  False
  AMGN           88.24               17            0.92              2.11        328.22                20.27         0.531          pass              0.487             55.8                           0.743                0.53              0.035                                 ok            True                  False
  INTC           95.65               23            2.46              1.88        108.52                88.85         0.529          pass              0.683             47.9                           0.483               -1.41             -0.162                                 ok            True                  False
  INSM           44.44                9            4.40              3.27        104.63               110.78         0.659          pass              0.110             14.6                           0.194               -5.40             -0.343            downtrend_blocked_slope           False                  False
   WMT           83.33               18            1.19              0.95        114.19                32.65         0.559          pass              0.262             21.4                           0.277              -15.07             -1.701 downtrend_blocked_slope_and_streak           False                  False
    ZS           66.67                3            8.56              9.33        151.71               157.27         0.549          pass              0.085             10.1                           0.219              -18.50             -2.796            downtrend_blocked_slope           False                  False
   HON           75.00                8            1.59              2.63        235.41                24.20         0.540          pass              0.079              8.4                           0.162                7.16              0.958                                 ok           False                  False
  REGN           88.24               34            0.61              2.56        599.56                42.53         0.538          pass              0.613             60.0                           0.673               -5.05             -0.633 downtrend_blocked_slope_and_streak           False                  False
  SHOP           66.67                9            4.87              4.24        122.30                84.68         0.511          pass              0.074              7.6                           0.185               15.31              1.931                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                 detail
2026-06-02T10:35:04.553797-04:00 early_entry_1035           entry_skipped                                                                                                                                                                                                                             {"reason": "no_candidate"}
2026-06-02T10:30:04.405006-04:00 early_entry_1030           entry_skipped                                                                                                                                                                                                                             {"reason": "no_candidate"}
2026-06-02T10:25:01.235572-04:00 early_entry_1025           entry_skipped                                                                                                                                                                                                                             {"reason": "no_candidate"}
2026-06-02T10:20:01.327977-04:00 early_entry_1020           entry_skipped                                                                                                                                                                                                                             {"reason": "no_candidate"}
2026-06-02T10:15:02.269482-04:00 early_entry_1015           entry_skipped                                                                                                                                                                                                 {"reason": "no_trade_after_option_and_timing_filters"}
2026-06-02T10:15:02.269482-04:00 early_entry_1015 entry_candidate_skipped {"early_entry_score": 0.679, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 117.0, "option_spread_pct": 24.24, "option_volume": 5.0, "reason": "no_trade_low_option_liquidity", "ticker": "CHTR", "timing_score": 0.442}
2026-06-02T10:10:06.260122-04:00 early_entry_1010           entry_skipped                                                                                                                                                                                                                             {"reason": "no_candidate"}
2026-06-02T10:05:01.451088-04:00 early_entry_1005           entry_skipped                                                                                                                                                                                                                             {"reason": "no_candidate"}
2026-06-02T10:00:02.499087-04:00 early_entry_1000           entry_skipped                                                                                                                                                                                                                             {"reason": "no_candidate"}
2026-06-02T09:20:05.650957-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                          {'saved': 92}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260602103504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260602103504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260602103504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260602103504)

</details>
