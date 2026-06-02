# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-02 10:25:01 EDT`
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
  FTNT          100.00               15            1.93              1.99        146.29                71.69         0.675          pass              0.666             55.1                           0.762               14.07              1.239                                 ok            True                  False
  MNST           95.00               20            1.31              0.82         88.75                49.60         0.632          pass              0.581             17.0                           0.251               -0.69              0.180                                 ok            True                  False
  MELI           92.00               25            1.67             20.23       1722.31                60.28         0.603          pass              0.610             43.3                           0.647                7.32              0.728                                 ok            True                  False
  AMGN           88.24               17            1.00              2.30        328.14                20.27         0.525          pass              0.474             51.8                           0.675                0.45              0.031                                 ok            True                  False
  INSM           50.00               10            4.26              3.16        104.67               110.78         0.667          pass              0.119             17.4                           0.244               -5.26             -0.336            downtrend_blocked_slope           False                  False
    ZS          100.00                2            8.75              9.53        151.62               157.27         0.583          pass              0.483              8.2                           0.343              -18.66             -2.805            downtrend_blocked_slope           False                  False
   WMT           84.21               19            1.10              0.88        114.22                32.65         0.559          pass              0.310             27.2                           0.277              -15.00             -1.697 downtrend_blocked_slope_and_streak           False                  False
   HON           78.57               14            1.07              1.78        235.78                24.20         0.541          pass              0.143             20.9                           0.193                7.72              0.982                                 ok           False                  False
  REGN           87.88               33            0.75              3.14        599.31                42.53         0.535          pass              0.570             50.9                           0.617               -5.18             -0.639 downtrend_blocked_slope_and_streak           False                  False
  UPRO           94.29               35            0.21              0.22        150.20                29.00         0.525          pass              0.849             83.1                           0.763                7.62              0.937                                 ok           False                  False
   CEG           81.58               38            0.24              0.46        265.50                57.21         0.523          pass              0.545             88.0                           0.541                1.16              0.171                                 ok           False                  False
  SHOP           66.67                9            4.71              4.09        122.37                84.68         0.523          pass              0.085             10.8                           0.308               15.52              1.939                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                 detail
2026-06-02T10:25:01.235572-04:00 early_entry_1025           entry_skipped                                                                                                                                                                                                                             {"reason": "no_candidate"}
2026-06-02T10:20:01.327977-04:00 early_entry_1020           entry_skipped                                                                                                                                                                                                                             {"reason": "no_candidate"}
2026-06-02T10:15:02.269482-04:00 early_entry_1015           entry_skipped                                                                                                                                                                                                 {"reason": "no_trade_after_option_and_timing_filters"}
2026-06-02T10:15:02.269482-04:00 early_entry_1015 entry_candidate_skipped {"early_entry_score": 0.679, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 117.0, "option_spread_pct": 24.24, "option_volume": 5.0, "reason": "no_trade_low_option_liquidity", "ticker": "CHTR", "timing_score": 0.442}
2026-06-02T10:10:06.260122-04:00 early_entry_1010           entry_skipped                                                                                                                                                                                                                             {"reason": "no_candidate"}
2026-06-02T10:05:01.451088-04:00 early_entry_1005           entry_skipped                                                                                                                                                                                                                             {"reason": "no_candidate"}
2026-06-02T10:00:02.499087-04:00 early_entry_1000           entry_skipped                                                                                                                                                                                                                             {"reason": "no_candidate"}
2026-06-02T09:20:05.650957-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                          {'saved': 92}
2026-06-01T15:10:04.135705-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-06-01T15:05:05.129733-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                        {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260602102501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260602102501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260602102501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260602102501)

</details>
