# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-12 15:05:11 EDT`
Last processed slot: `entry_1500`

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

- Cash: `$27,308.25`
- Equity: `$27,308.25`
- Realized PnL: `$17,308.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-06-12)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MPWR           93.75               32            0.85              9.44       1585.51                71.83         0.570            pass              0.741             57.0                           0.426                2.18             -0.350                                 ok            True                  False
  ASML           93.33               30            1.18             15.63       1892.78                60.86         0.523            pass              0.757             71.8                           0.584               15.26              1.313                                 ok            True                   True
  ISRG           81.48               27            1.09              3.14        411.55                34.54         0.500 below_threshold              0.371             55.9                           0.562               -0.93              0.027                                 ok            True                  False
  INTU           81.25               32            1.35              2.62        275.79               100.42         0.718            pass              0.426             57.9                           0.517              -22.78             -2.206 downtrend_blocked_slope_and_streak           False                  False
    MU           81.58               38            0.22              1.55        995.21               115.24         0.696            pass              0.582             94.5                           0.676               -4.04             -0.762                                 ok           False                  False
  AVGO           83.87               31            1.03              2.78        384.38                69.71         0.595            pass              0.464             53.7                           0.613              -17.04             -2.491            downtrend_blocked_slope           False                  False
  TEAM           84.38               32            1.84              1.15         88.71                85.01         0.544            pass              0.507             63.1                           0.532              -24.48             -2.642 downtrend_blocked_slope_and_streak           False                  False
  AAPL          100.00               10            1.63              3.37        294.18                23.83         0.536            pass              0.513             19.8                           0.448               -5.06             -0.822            downtrend_blocked_slope           False                  False
  CSCO           94.44               36            0.38              0.33        121.69                43.07         0.527            pass              0.747             45.3                           0.410                0.03             -0.465                                 ok           False                  False
  CRWD           80.00               35            0.78              3.77        689.91                64.88         0.524            pass              0.400             60.2                           0.427              -12.28             -1.436 downtrend_blocked_slope_and_streak           False                  False
  CTAS          100.00                2            3.10              3.94        180.19                29.28         0.522            pass              0.507             18.4                           0.193                1.94              0.284                                 ok           False                  False
  WDAY           83.33               30            1.54              1.41        129.93                70.45         0.503            pass              0.463             63.6                           0.579              -18.26             -1.923 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et         slot              event_type                                                                                                                                                                                                                                                  detail
2026-06-12T15:05:11.809096-04:00   entry_1500            slot_skipped                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-06-12T15:00:11.776390-04:00   entry_1500            slot_skipped                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-06-12T14:55:11.337200-04:00   entry_1500            slot_skipped                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-06-12T14:50:07.527766-04:00   entry_1500           entry_skipped                                                                                                                                                            {"budget": 13654.13, "entry_cost": 15345.0, "reason": "insufficient_cash", "ticker": "ASML"}
2026-06-12T14:50:07.527766-04:00   entry_1500 entry_candidate_skipped {"early_entry_score": 0.73, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 0.0, "option_spread_pct": 7.0, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "MPWR", "timing_score": 0.565}
2026-06-12T14:50:07.527766-04:00   entry_1500          timing_overlay                                                                                                                                            {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-06-12", "training_samples": 5261, "window": 5}
2026-06-12T13:30:06.922165-04:00 data_refresh            data_refresh                                                                                                                                                                                                                                           {'saved': 93}
2026-06-11T16:00:02.840701-04:00  manage_1600                    exit                                                                       {"asset_type": "option", "contract_symbol": "PAYX260717C00100000", "fill_price": 4.725, "pnl": -1417.5, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "PAYX"}
2026-06-11T15:10:05.901456-04:00   entry_1500            slot_skipped                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-06-11T15:05:01.637462-04:00   entry_1500            slot_skipped                                                                                                                                                                                                                         {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260612150511)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260612150511)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260612150511)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260612150511)

</details>
