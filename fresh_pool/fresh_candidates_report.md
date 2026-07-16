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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-83MS` (url=410ms, nekobox=430ms, status=yes)
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-87MS` (url=336ms, nekobox=392ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-95MS` (url=341ms, nekobox=376ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-104MS` (url=423ms, nekobox=392ms, status=yes)
5. `AKUN-005-RS-RAPIDSEEDBOX-20190717-VLESS-WS-109MS` (url=379ms, nekobox=450ms, status=yes)
6. `AKUN-006-DIXONS-VLESS-WS-112MS` (url=365ms, nekobox=382ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-118MS` (url=307ms, nekobox=326ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-104MS` (url=370ms, nekobox=361ms, status=yes)
9. `AKUN-009-DEV-VLESS-WS-102MS` (url=314ms, nekobox=329ms, status=yes)
10. `AKUN-010-WEBEX-VLESS-WS-131MS` (url=490ms, nekobox=354ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-117MS` (url=303ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-157MS` (url=395ms, status=HTTP 204)
13. `AKUN-013-NEXUSMODS-VLESS-WS-162MS` (url=378ms, status=HTTP 204)
14. `AKUN-014-466688-VLESS-WS-119MS` (url=358ms, status=HTTP 204)
15. `AKUN-015-DEV-VLESS-WS-126MS` (url=302ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-109MS` (url=328ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-142MS` (url=378ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-112MS` (url=384ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-108MS` (url=392ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-175MS` (url=378ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-182MS` (url=347ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-101MS` (url=384ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-106MS` (url=303ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-132MS` (url=480ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-116MS` (url=322ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
