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
1. `AKUN-001-UNKNOWN-VLESS-WS-107MS` (url=293ms, nekobox=290ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-117MS` (url=290ms, nekobox=314ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-114MS` (url=276ms, nekobox=313ms, status=yes)
4. `AKUN-004-NETCUP-VLESS-WS-110MS` (url=308ms, nekobox=357ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-132MS` (url=285ms, nekobox=292ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-119MS` (url=310ms, nekobox=286ms, status=yes)
7. `AKUN-007-UK-GB-DCL-01-20191003-VLESS-WS-135MS` (url=332ms, nekobox=304ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-140MS` (url=263ms, nekobox=334ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-101MS` (url=271ms, nekobox=330ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-111MS` (url=279ms, nekobox=291ms, status=yes)
11. `AKUN-011-WPENG-VLESS-WS-118MS` (url=277ms, status=HTTP 204)
12. `AKUN-012-ZVC-VLESS-WS-112MS` (url=294ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-121MS` (url=363ms, status=HTTP 204)
14. `AKUN-014-WPENG-VLESS-WS-133MS` (url=289ms, status=HTTP 204)
15. `AKUN-015-WEYRO-NET-VLESS-WS-142MS` (url=320ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-142MS` (url=244ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-154MS` (url=272ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-129MS` (url=277ms, status=HTTP 204)
19. `AKUN-020-SPEEDTEST-VLESS-WS-317MS` (url=594ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-297MS` (url=703ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-329MS` (url=732ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-343MS` (url=780ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-327MS` (url=695ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-364MS` (url=668ms, status=HTTP 204)
25. `AKUN-027-CLOUDFLARE-VLESS-WS-494MS` (url=959ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
