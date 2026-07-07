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
1. `AKUN-001-UNKNOWN-VLESS-WS-98MS` (url=256ms, nekobox=315ms, status=yes)
2. `AKUN-002-INTERNETWORKS-45-131-208-VLESS-WS-113MS` (url=276ms, nekobox=306ms, status=yes)
3. `AKUN-003-WPENG-VLESS-WS-110MS` (url=284ms, nekobox=288ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-109MS` (url=292ms, nekobox=316ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-116MS` (url=337ms, nekobox=304ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-115MS` (url=260ms, nekobox=315ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-91MS` (url=314ms, nekobox=281ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-118MS` (url=241ms, nekobox=310ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-121MS` (url=310ms, nekobox=304ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-121MS` (url=241ms, nekobox=236ms, status=no)
11. `AKUN-010-CLOUDFLARE-VLESS-WS-108MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-129MS` (url=281ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-133MS` (url=259ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-135MS` (url=252ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-122MS` (url=289ms, status=HTTP 204)
16. `AKUN-016-466688-VLESS-WS-149MS` (url=272ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-127MS` (url=250ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-165MS` (url=245ms, status=HTTP 204)
19. `AKUN-019-WPENG-VLESS-WS-96MS` (url=280ms, status=HTTP 204)
20. `AKUN-020-WEYRO-NET-VLESS-WS-133MS` (url=324ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-126MS` (url=384ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-266MS` (url=429ms, status=HTTP 204)
23. `AKUN-023-GALAKTIKA-20201015-VLESS-WS-322MS` (url=649ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-319MS` (url=707ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-306MS` (url=667ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
