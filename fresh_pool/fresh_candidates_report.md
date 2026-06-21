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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-69MS` (url=228ms, nekobox=178ms, status=no)
2. `AKUN-001-CLOUDFLARE-VLESS-WS-70MS`
3. `AKUN-002-CLOUDFLARE-VLESS-WS-72MS`
4. `AKUN-003-UNKNOWN-VLESS-WS-77MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-77MS`
6. `AKUN-005-CLOUDWEBMANAGE-EU-FR-VLESS-WS-70MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-78MS`
8. `AKUN-007-US-VLESS-WS-80MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-95MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-101MS`
11. `AKUN-010-EE-WELCOMEHOST-20190515-VLESS-WS-79MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-82MS` (url=205ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-86MS` (url=220ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-84MS` (url=230ms, status=HTTP 204)
15. `AKUN-015-1PASSWORD-VLESS-WS-80MS` (url=208ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-109MS` (url=202ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-105MS` (url=210ms, status=HTTP 204)
18. `AKUN-018-ADF-VLESS-WS-111MS` (url=197ms, status=HTTP 204)
19. `AKUN-019-RS-RAPIDSEEDBOX-20190717-VLESS-WS-131MS` (url=218ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-131MS` (url=201ms, status=HTTP 204)
21. `AKUN-021-DEV-VLESS-WS-246MS` (url=508ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-357MS` (url=742ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-389MS` (url=835ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-397MS` (url=838ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-375MS` (url=835ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
