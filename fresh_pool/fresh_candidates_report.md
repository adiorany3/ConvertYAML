# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 25
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 31

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-126MS` (url=263ms, nekobox=300ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-127MS` (url=252ms, nekobox=282ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-130MS` (url=252ms, nekobox=229ms, status=no)
4. `AKUN-004-DEV-VLESS-WS-135MS` (url=250ms, nekobox=232ms, status=no)
5. `AKUN-003-CLOUDFLARE-VLESS-WS-136MS`
6. `AKUN-004-CLOUDWEBMANAGE-EU-FR-VLESS-WS-136MS`
7. `AKUN-005-COMPREND-NET-VLESS-WS-140MS`
8. `AKUN-006-CLOUDFLARE-VLESS-WS-142MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-141MS` (url=261ms, nekobox=234ms, status=no)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-144MS` (url=247ms, nekobox=234ms, status=no)
11. `AKUN-007-COMPREND-NET-VLESS-WS-147MS`
12. `AKUN-008-UNKNOWN-VLESS-WS-133MS`
13. `AKUN-013-CLOUDFLARE-VLESS-WS-144MS` (url=243ms, nekobox=229ms, status=no)
14. `AKUN-009-COMPREND-NET-VLESS-WS-153MS`
15. `AKUN-010-CLOUDFLARE-VLESS-WS-164MS`
16. `AKUN-016-CLOUDFLARE-VLESS-WS-169MS` (url=303ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-141MS` (url=286ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-144MS` (url=275ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-362MS` (url=700ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-364MS` (url=693ms, status=HTTP 204)
21. `AKUN-021-UK-GB-DCL-01-20191003-VLESS-WS-141MS` (url=325ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-393MS` (url=784ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-405MS` (url=774ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-390MS` (url=773ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-391MS` (url=766ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
