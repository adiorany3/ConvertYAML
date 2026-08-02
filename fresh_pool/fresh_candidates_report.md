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
- Proxy di openclash_fresh_pool.yaml: 29

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
1. `AKUN-001-UNKNOWN-VLESS-WS-56MS` (url=247ms, nekobox=235ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-62MS` (url=212ms, nekobox=236ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-65MS` (url=218ms, nekobox=236ms, status=yes)
4. `AKUN-004-ZENFO-1-VLESS-WS-67MS` (url=215ms, nekobox=245ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-56MS` (url=208ms, nekobox=239ms, status=yes)
6. `AKUN-006-NOTION-WEB-VLESS-WS-63MS` (url=219ms, nekobox=7177ms, status=no)
7. `AKUN-006-CLOUDFLARE-VLESS-WS-64MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-69MS`
9. `AKUN-008-EE-WELCOMEHOST-20190515-VLESS-WS-67MS`
10. `AKUN-009-UNKNOWN-VLESS-WS-70MS`
11. `AKUN-011-CLOUDFLARE-VLESS-WS-66MS` (url=213ms, nekobox=173ms, status=no)
12. `AKUN-010-CLOUDFLARE-VLESS-WS-56MS`
13. `AKUN-013-EU-VLESS-WS-60MS` (url=209ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-67MS` (url=208ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-102MS` (url=204ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-72MS` (url=329ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-110MS` (url=206ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-133MS` (url=209ms, status=HTTP 204)
19. `AKUN-019-RMGYVPN-VLESS-WS-269MS` (url=558ms, status=HTTP 204)
20. `AKUN-020-LEVIKOGJGFDD-VLESS-WS-344MS` (url=739ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-491MS` (url=990ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-499MS` (url=990ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-555MS` (url=1135ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-529MS` (url=1225ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-596MS` (url=1072ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
