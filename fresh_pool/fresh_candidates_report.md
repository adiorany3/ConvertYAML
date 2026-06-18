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
1. `AKUN-001-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-60MS` (url=224ms, nekobox=228ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-64MS` (url=197ms, nekobox=243ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-68MS` (url=209ms, nekobox=187ms, status=no)
4. `AKUN-003-CLOUDFLARE-VLESS-WS-74MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-88MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-71MS`
7. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-65MS`
8. `AKUN-007-1PASSWORD-VLESS-WS-70MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-80MS`
10. `AKUN-010-CLOUDFLARE-VLESS-WS-72MS` (url=200ms, nekobox=181ms, status=no)
11. `AKUN-009-CLOUDFLARE-VLESS-WS-68MS`
12. `AKUN-010-CLOUDFLARE-VLESS-WS-89MS`
13. `AKUN-013-CLOUDFLARE-VLESS-WS-80MS` (url=213ms, status=HTTP 204)
14. `AKUN-014-RS-RAPIDSEEDBOX-20190717-VLESS-WS-91MS` (url=214ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-116MS` (url=219ms, status=HTTP 204)
16. `AKUN-016-OPENAI-VLESS-WS-113MS` (url=198ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-127MS` (url=203ms, status=HTTP 204)
18. `AKUN-018-MEDIUM-VLESS-WS-93MS` (url=196ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-117MS` (url=228ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-88MS` (url=198ms, status=HTTP 204)
21. `AKUN-021-MYBB-VLESS-WS-105MS` (url=199ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-374MS` (url=746ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-407MS` (url=802ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-416MS` (url=840ms, status=HTTP 204)
25. `AKUN-026-ADF-VLESS-WS-84MS` (url=196ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
