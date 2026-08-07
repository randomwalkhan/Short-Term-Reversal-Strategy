# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-07 10:10:01 EDT`
Last processed slot: `manage_1000`

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

- Cash: `$17,608.25`
- Equity: `$33,508.25`
- Realized PnL: `$24,370.75`
- Unrealized PnL: `$-862.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  INTC     option         option INTC260918C00100000       2026-08-06                   1     15     16762.5                 15900.0        11.18           10.6      100.37         99.08          bid_ask_mid                       10.6                bid_ask_mid                    True          -862.5                  -5.15          85.0               40              0.68         79.69            81.1                  86.71               28020.0         1406.0               0.03                      ok
```

## Today's Closed Trades (2026-08-07)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MRVL           80.56               36            0.72              1.07        210.08                99.17         0.640          pass              0.349             32.2                           0.184                7.61              1.821                                 ok            True                  False
  TMUS           90.62               32            0.78              0.99        179.55                57.01         0.606          pass              0.661             56.7                           0.642               -0.85             -0.144                                 ok            True                  False
  INTC           84.62               39            0.79              0.55         99.57                86.24         0.583          pass              0.449             24.8                           0.123                7.26              1.436                                 ok            True                  False
    MU           82.76               29            3.12             19.27        873.21               110.38         0.551          pass              0.255              0.0                           0.150               -7.28              0.107                                 ok            True                  False
  INSM           66.67               18            2.44              2.27        131.58               110.04         0.738          pass              0.152              8.2                           0.198               20.94              1.477                                 ok           False                  False
  LRCX           89.47               38            0.16              0.34        305.63                89.60         0.664          pass              0.712             68.7                           0.309                0.03              0.941                                 ok           False                  False
  ALNY           85.29               34            1.01              1.52        215.47               128.30         0.625          pass              0.548             61.4                           0.537              -21.28             -3.066            downtrend_blocked_slope           False                  False
   CSX           91.67               24            0.73              0.26         50.59                29.04         0.547          pass              0.586             42.2                           0.386               -5.45             -0.314 downtrend_blocked_slope_and_streak           False                  False
  DRAM           76.00               25            4.29              1.54         50.78               108.98         0.518          pass              0.152              0.0                           0.150               -7.45              0.246                                 ok           False                  False
  CTSH           88.10               42            0.02              0.01         56.89                55.66         0.514          pass              0.765             99.2                           0.559               25.15              2.018                                 ok           False                  False
   ADP           97.22               36            0.01              0.01        273.51                34.67         0.511          pass              0.924             99.8                           0.730                9.36              0.724                                 ok           False                  False
 GOOGL           79.07               43            0.52              1.31        357.19                51.28         0.507          pass              0.375             41.4                           0.370               11.30              1.355                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            detail
2026-08-07T10:10:01.433730-04:00 early_entry_1010 early_entry_shadow {"contract_symbol": "ORLY260918C00093330", "current_drop_pct": 0.58, "early_entry_score": 0.726, "early_reclaim_pct": 84.8, "entry_ask": 3.8, "entry_bid": 2.6, "entry_mode": "early", "entry_option_price": 3.2, "hypothetical_budget": 8804.13, "hypothetical_contracts": 27, "matched_signals": 37, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 254.0, "option_spread_pct": 37.5, "option_volume": 17.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.748, "shadow_only": true, "success_rate": 89.19, "ticker": "ORLY", "timing_score": 0.465, "top_candidates": [{"current_drop_pct": 0.58, "early_entry_score": 0.726, "early_reclaim_pct": 84.8, "matched_signals": 37, "recovery_stability_score": 0.748, "success_rate": 89.19, "ticker": "ORLY", "timing_score": 0.465, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-07T10:05:05.478835-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-07T10:00:04.307079-04:00 early_entry_1000 early_entry_shadow {"contract_symbol": "ORLY260918C00093330", "current_drop_pct": 0.71, "early_entry_score": 0.701, "early_reclaim_pct": 81.6, "entry_ask": 3.8, "entry_bid": 2.6, "entry_mode": "early", "entry_option_price": 3.2, "hypothetical_budget": 8804.13, "hypothetical_contracts": 27, "matched_signals": 36, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 254.0, "option_spread_pct": 37.5, "option_volume": 17.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.651, "shadow_only": true, "success_rate": 88.89, "ticker": "ORLY", "timing_score": 0.463, "top_candidates": [{"current_drop_pct": 0.71, "early_entry_score": 0.701, "early_reclaim_pct": 81.6, "matched_signals": 36, "recovery_stability_score": 0.651, "success_rate": 88.89, "ticker": "ORLY", "timing_score": 0.463, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-07T00:00:06.807009-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {'saved': 93}
2026-08-06T15:10:06.321105-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-08-06T15:05:05.205099-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-08-06T15:00:02.209761-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-08-06T14:55:01.108594-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-08-06T14:50:04.202564-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"allocated_cash": 16762.5, "asset_type": "option", "contract_symbol": "INTC260918C00100000", "contracts": 15, "early_entry_score": 0.652, "entry_mode": "regular", "entry_option_price": 11.175, "execution_mode": "option", "matched_signals": 40, "option_liquidity_status": "ok", "option_open_interest": 28020.0, "option_spread_pct": 3.13, "option_volume": 1406.0, "success_rate": 85.0, "ticker": "INTC", "timing_score": 0.565}
2026-08-06T14:50:04.202564-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-08-06", "training_samples": 5584, "window": 5}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260807101001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260807101001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260807101001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260807101001)

</details>
