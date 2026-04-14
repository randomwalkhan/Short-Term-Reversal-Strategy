# Reversal 3.2.2 Live Paper Test

Latest checkpoint (ET): `2026-04-14 14:05:06 EDT`
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
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`; off-hours `5-minute` checkpoints continue mark-to-market updates for open positions, while share-fallback positions also run take-profit and stop loss scans in after-hours / overnight / pre-market
- Live exit ladder: `+15% / +15% / -12%`
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Fallback execution: buy shares when the option fails the liquidity gate; use `+3% / -3%` for common-stock fallback and `+5% / -5%` for leveraged-ETF shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; share positions can additionally trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries and exits use the current option mark price; no intraday future path is assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$7,229.00`
- Equity: `$13,245.72`
- Realized PnL: `$3,145.00`
- Unrealized PnL: `$100.72`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct      option_liquidity_status
  REGN      share share_fallback       REGN       2026-04-13                   1      8      5916.0                 6016.72        739.5         752.09       739.5        752.09          100.72                    1.7         100.0               24              1.25           NaN             NaN                  24.22                  89.0            1.0               0.07 low_open_interest,low_volume
```

## Today's Closed Trades (2026-04-14)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  FANG          100.00               16            1.71              2.26        188.13                30.53            True
  INTC           95.24               21            3.42              1.56         64.53                75.15            True
  FAST           92.86               14            2.00              0.64         45.53                37.61            True
  MPWR           91.18               34            0.93              8.96       1368.39                58.48            True
  ORLY           90.70               43            0.52              0.34         93.86                24.40            True
  COST           90.32               31            0.62              4.26        979.02                19.04            True
  CTSH           85.37               41            0.51              0.22         60.44                30.13            True
  WDAY           80.00               30            1.95              1.63        119.22                50.72            True
  PCAR           80.00               20            1.41              1.26        126.84                27.21            True
  TMUS           80.00               15            1.58              2.13        191.52                20.34            True
   HON          100.00               27            0.42              0.69        233.35                23.77           False
   LIN          100.00                3            2.47              8.81        505.10                18.23           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-14T14:05:06.440824-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-14T14:00:05.431636-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-14T13:55:04.952325-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-14T13:40:06.435598-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-14T13:35:06.418066-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-14T13:30:06.417621-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-14T13:25:06.439003-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-14T13:10:06.425309-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-14T13:05:06.417007-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-14T13:00:06.426810-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.2 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260414140506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.2 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260414140506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.2 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260414140506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.2 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260414140506)

</details>
