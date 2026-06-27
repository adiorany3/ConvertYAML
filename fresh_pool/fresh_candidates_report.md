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
1. `AKUN-001-VULTR-VLESS-WS-95MS` (url=202ms, nekobox=251ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-125MS` (url=225ms, nekobox=258ms, status=yes)
3. `AKUN-003-DEV-VLESS-WS-106MS` (url=231ms, nekobox=274ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-121MS` (url=232ms, nekobox=264ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-127MS` (url=251ms, nekobox=277ms, status=yes)
6. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-129MS` (url=205ms, nekobox=276ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-134MS` (url=245ms, nekobox=278ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-134MS` (url=230ms, nekobox=248ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-138MS` (url=261ms, nekobox=284ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-156MS` (url=247ms, nekobox=273ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-115MS` (url=210ms, status=HTTP 204)
12. `AKUN-012-CLOUDWEBMANAGE-EU-FR-VLESS-WS-141MS` (url=251ms, status=HTTP 204)
13. `AKUN-013-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-98MS` (url=260ms, status=HTTP 204)
14. `AKUN-014-US-VLESS-WS-131MS` (url=256ms, status=HTTP 204)
15. `AKUN-015-ZVC-VLESS-WS-126MS` (url=266ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-115MS` (url=331ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-167MS` (url=268ms, status=HTTP 204)
18. `AKUN-018-COMPREND-NET-VLESS-WS-157MS` (url=237ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-168MS` (url=241ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-179MS` (url=228ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-397MS` (url=799ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-316MS` (url=625ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-427MS` (url=886ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-408MS` (url=853ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-432MS` (url=826ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
