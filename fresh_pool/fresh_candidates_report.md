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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-93MS` (url=272ms, nekobox=322ms, status=yes)
2. `AKUN-002-WPENG-VLESS-WS-99MS` (url=307ms, nekobox=251ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-96MS` (url=333ms, nekobox=265ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-99MS` (url=245ms, nekobox=290ms, status=yes)
5. `AKUN-005-SAINT-PETERSBURG-VLESS-WS-79MS` (url=254ms, nekobox=289ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-88MS` (url=244ms, nekobox=273ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-81MS` (url=307ms, nekobox=305ms, status=yes)
8. `AKUN-008-WEYRO-NET-VLESS-WS-111MS` (url=240ms, nekobox=309ms, status=yes)
9. `AKUN-009-WPENG-VLESS-WS-116MS` (url=284ms, nekobox=274ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-89MS` (url=250ms, nekobox=281ms, status=yes)
11. `AKUN-011-ALIBABA-VLESS-WS-107MS` (url=220ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-94MS` (url=254ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-77MS` (url=237ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-136MS` (url=276ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-115MS` (url=247ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-85MS` (url=292ms, status=HTTP 204)
17. `AKUN-018-UNKNOWN-VLESS-WS-274MS` (url=560ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-280MS` (url=608ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-276MS` (url=740ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-297MS` (url=607ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-299MS` (url=576ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-302MS` (url=649ms, status=HTTP 204)
23. `AKUN-025-SPEEDTEST-VLESS-WS-273MS` (url=553ms, status=HTTP 204)
24. `AKUN-027-CLOUDFLARE-VLESS-WS-483MS` (url=777ms, status=HTTP 204)
25. `AKUN-029-UNKNOWN-VLESS-WS-517MS` (url=832ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
