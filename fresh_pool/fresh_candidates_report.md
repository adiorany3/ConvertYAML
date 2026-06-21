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
1. `AKUN-001-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-120MS` (url=245ms, nekobox=277ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-117MS` (url=283ms, nekobox=271ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-114MS` (url=274ms, nekobox=295ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-118MS` (url=251ms, nekobox=310ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-113MS` (url=246ms, nekobox=276ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-120MS` (url=241ms, nekobox=282ms, status=yes)
7. `AKUN-007-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-120MS` (url=273ms, nekobox=321ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-154MS` (url=282ms, nekobox=289ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-106MS` (url=297ms, nekobox=275ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-129MS` (url=238ms, nekobox=221ms, status=no)
11. `AKUN-010-CLOUDFLARE-VLESS-WS-135MS`
12. `AKUN-012-VULTR-VLESS-WS-102MS` (url=238ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-134MS` (url=248ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-304MS` (url=683ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-339MS` (url=697ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-328MS` (url=746ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-338MS` (url=701ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-364MS` (url=663ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-361MS` (url=742ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-237MS` (url=1187ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-337MS` (url=811ms, status=HTTP 204)
22. `AKUN-031-CLOUDFLARE-VLESS-WS-699MS` (url=1069ms, status=HTTP 204)
23. `AKUN-032-UNKNOWN-VLESS-WS-642MS` (url=1013ms, status=HTTP 204)
24. `AKUN-033-DEV-VLESS-WS-610MS` (url=728ms, status=HTTP 204)
25. `AKUN-034-UNKNOWN-VLESS-WS-722MS` (url=742ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
