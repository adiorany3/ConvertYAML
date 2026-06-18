# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 19
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 25

## Cara Pakai di OpenWrt
Jalankan manual saat node mulai mati:

```sh
sh /etc/mihomo-autopilot/openwrt_pull_fresh_pool.sh
```

Atau aktifkan guard otomatis:

```sh
sh /etc/mihomo-autopilot/openwrt_fresh_guard.sh
```

## Kandidat Fresh Teratas
1. `AKUN-001-CLOUDFLARE-VLESS-WS-109MS` (url=248ms, nekobox=274ms, status=yes)
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-112MS` (url=260ms, nekobox=276ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-115MS` (url=275ms, nekobox=218ms, status=no)
4. `AKUN-003-CLOUDFLARE-VLESS-WS-122MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-134MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-116MS`
7. `AKUN-006-CLOUDWEBMANAGE-EU-FR-VLESS-WS-126MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-140MS`
9. `AKUN-008-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-143MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-344MS`
11. `AKUN-010-CONFLU-VLESS-WS-356MS`
12. `AKUN-013-UNKNOWN-VLESS-WS-359MS` (url=765ms, status=HTTP 204)
13. `AKUN-014-CLOUDFLARE-VLESS-WS-328MS` (url=655ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-375MS` (url=2422ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-375MS` (url=635ms, status=HTTP 204)
16. `AKUN-019-CLOUDFLARE-VLESS-WS-147MS` (url=283ms, status=HTTP 204)
17. `AKUN-025-CLOUDFLARE-VLESS-WS-589MS` (url=701ms, status=HTTP 204)
18. `AKUN-030-SPEEDTEST-VLESS-WS-889MS` (url=1259ms, status=HTTP 204)
19. `AKUN-033-CLOUDFLARE-VLESS-WS-123MS` (url=232ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
