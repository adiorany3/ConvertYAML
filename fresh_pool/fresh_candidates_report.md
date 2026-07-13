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
- Proxy di openclash_fresh_pool.yaml: 30

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-82MS` (url=302ms, nekobox=314ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-100MS` (url=377ms, nekobox=313ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-113MS` (url=327ms, nekobox=467ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-103MS` (url=290ms, nekobox=322ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-99MS` (url=312ms, nekobox=7177ms, status=no)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-114MS` (url=299ms, nekobox=241ms, status=no)
7. `AKUN-005-CLOUDFLARE-VLESS-WS-130MS`
8. `AKUN-006-CLOUDFLARE-VLESS-WS-133MS`
9. `AKUN-007-466688-VLESS-WS-125MS`
10. `AKUN-008-CLOUDFLARE-VLESS-WS-140MS`
11. `AKUN-009-CLOUDFLARE-VLESS-WS-137MS`
12. `AKUN-010-CLOUDFLARE-VLESS-WS-144MS`
13. `AKUN-013-UNKNOWN-VLESS-WS-146MS` (url=307ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-156MS` (url=348ms, status=HTTP 204)
15. `AKUN-015-DPDNS-VLESS-WS-162MS` (url=384ms, status=HTTP 204)
16. `AKUN-016-HETZNER-VLESS-WS-152MS` (url=350ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-155MS` (url=294ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-141MS` (url=296ms, status=HTTP 204)
19. `AKUN-019-HETZNER-VLESS-WS-153MS` (url=297ms, status=HTTP 204)
20. `AKUN-020-PUBLICDOMAINREGISTRY-NET-VLESS-WS-148MS` (url=389ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-309MS` (url=616ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-344MS` (url=728ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-354MS` (url=2301ms, status=HTTP 204)
24. `AKUN-026-CLOUDFLARE-VLESS-WS-342MS` (url=1549ms, status=HTTP 204)
25. `AKUN-028-CLOUDFLARE-VLESS-WS-226MS` (url=857ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
